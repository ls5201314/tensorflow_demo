from numpy import *

class cluster_node:
    def __init__(self, vec, id, left=None, right=None, distance=0):
        self.vec = vec
        self.left = left
        self.right = right
        self.distance = distance
        self.id = id

def L2dis(v1, v2):
    return sqrt(sum((v1-v2)**2))

def L1dis(v1, v2):
    return sum(abs(v1-v2))

def hCluster(features, distance=L2dis):
    distances = {}
    currentClusterId = -1
    cluster = [cluster_node(array(features[i]), i) for i in range(len(features))]
    while len(cluster) > 1:
        lowestpair = (0, 1)
        closest = distance(cluster[0].vec, cluster[1].vec)
        for i in range(len(cluster)):
            for j in range(i+1, len(cluster)):
                if (cluster[i].id, cluster[j].id) not in distances:
                    distances[(cluster[i].id, cluster[j].id)] = distance(cluster[i].vec, cluster[j].vec)

                d = distances[(cluster[i].id, cluster[j].id)]
                if d < closest:
                    lowestpair = (i, j)
                    closest = d

        mergeVec = [(cluster[lowestpair[0]].vec[index] + cluster[lowestpair[1]].vec[index]) / 2.0  for index in range(len(cluster[0].vec))]
        newClusterNode = cluster_node(array(mergeVec), currentClusterId, left=cluster[lowestpair[0]], right=cluster[lowestpair[1]], distance=closest)

        currentClusterId -= 1
        del cluster[lowestpair[1]]
        del cluster[lowestpair[0]]
        cluster.append(newClusterNode)

    return cluster[0]

def extract_clusters(cluster, dis):
    if cluster.distance < dis:
        return [cluster]
    else:
        cl = []
        cr = []
        if cluster.left != None:
            cl = extract_clusters(cluster.left, dis)
        if cluster.right != None:
            cr = extract_clusters(cluster.right, dis)
        return cl + cr

def get_cluster_elements(cluster):
    if cluster.id >= 0:
        return [cluster]
    else:
        cl = []
        cr = []
        if cluster.left != None:
            cl = get_cluster_elements(cluster.left)
        if cluster.right != None:
            cr = get_cluster_elements(cluster.right)

        return cl + cr

def print_cluster(cluster, labers=None, n=0):
    for i in range(n): print(" ")
    if cluster.id < 0:
        print("-")

    else:
        if labers == None: print(cluster.id)
        else: print(labers[cluster.id])
    if cluster.left != None: print_cluster(cluster.left, labers)
    if cluster.right != None: print_cluster(cluster.right, labers)

def getHeight(cluster):
    if cluster.left == None and cluster.right == None: return 1

    return getHeight(cluster.left) + getHeight(cluster.right)

def getDepth(cluster):
    if cluster.left == None and cluster.right == None: return 0

    return max(getDepth(cluster.left), getDepth(cluster.right)) + cluster.distance