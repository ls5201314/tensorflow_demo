from HierarchicalClustering import *
from PIL import Image, ImageDraw
import numpy as np
import os

def drawdendrogram(clust, imlist, jpeg="clusters.jpg"):

    h = getHeight(clust) * 20
    w = 1200
    depth = getDepth(clust)

    scaling = float(w-150) / depth

    img = Image.new("RGB", (w, h), (255,255,255))
    draw = ImageDraw.Draw(img)

    draw.line((0, h/2, 10, h/2), fill=(255, 0, 0))

    drawnode(draw, clust, 10, int(h/2), scaling, imlist, img)
    img.save(jpeg)

def drawnode(draw, clust, x, y, scaling, imlist, img):
    if clust.id < 0:
        h1 = getHeight(clust.left) * 20
        h2 = getHeight(clust.right) * 20
        top = y - (h1 + h2) / 2
        bottom = y + (h1 + h2) / 2

        ll = clust.distance * scaling
        draw.line((x, top + h1 / 2, x, bottom - h2 / 2), fill=(255, 0, 0))

        draw.line((x, top + h1 / 2, x + ll , top + h1 / 2), fill=(255, 0, 0))

        draw.line((x, bottom - h2 / 2, x + ll, bottom - h2 / 2), fill=(255, 0, 0))

        drawnode(draw, clust.left, x + ll, top + h1 / 2, scaling, imlist, img)
        drawnode(draw, clust.right, x + ll, bottom - h2 / 2, scaling, imlist, img)
    else:
        nodeimg = Image.open(imlist[clust.id])
        nodeimg.thumbnail((20, 20))
        ns = nodeimg.size
        print(x, y-ns[1]//2)
        print(x+ns[0])
        img.paste(nodeimg, (int(x), int(y-ns[1]//2), int(x+ns[0]), int(y+ns[1]-ns[1]//2)))

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

tree = hCluster(features, distance=L1dis)
drawdendrogram(tree, imlist, jpeg="sunset1.jpg")