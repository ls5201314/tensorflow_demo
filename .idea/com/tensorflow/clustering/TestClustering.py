from HierarchicalClustering import *
from PIL import Image, ImageDraw
import numpy as np
import os

imlist = []
folderPath = r'C:\Users\ls\Desktop\图片素材'

for filename in os.listdir(folderPath):
    if os.path.splitext(filename)[1] == '.jpg':
        imlist.append(os.path.join(folderPath, filename))
n = len(imlist)
print(n)

features = np.zeros((n, 3))
for i in range(n):
    im = np.array(Image.open(imlist[i]))
    R = np.mean(im[:, :, 0].flatten())
    G = np.mean(im[:, :, 1].flatten())
    B = np.mean(im[:, :, 2].flatten())
    features[i] = np.array([R, G, B])

tree = hCluster(features)
labers = [cluster_node(array(features[i]), i) for i in range(len(features))]
print_cluster(tree, labers=labers)