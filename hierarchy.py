import numpy as np
import pandas as pd

x = np.random.normal(loc=np.random.uniform(size=(5,))*10-5,size=(100,5))
#x2 = np.random.normal(loc=np.random.uniform(size=(5,))*10-5,size=(500,5))

#x = np.vstack((x1,x2))
shuffle = np.random.permutation(x.shape[0])
x = x[shuffle,:]
membership = shuffle.copy()
for i in range(len(membership)):
    if membership[i]<20: membership[i]=0
    elif membership[i]<40: membership[i]=1
    else: membership[i]=2
np.unique(membership,return_counts=True)
membership

dendogram = []


def hclust(x: np.array, dendogram: list, n: int):
    distmat = np.zeros((n,n))

    for i in range(n):
    	for j in range(n):
    	    distmat[i,j] = ((x[i,:]-x[j:])**2).sum()


    np.fill_diagonal(distmat, 9999)
    y1 = distmat.argmin(0).argmin()
    y2 = distmat.argmin(0)[distmat.argmin(0).argmin()]

    cluster = (x[y1,:] + x[y2,:])/2
    xcopy = x
    xcopy[y2] = cluster
    xcopy = np.delete(xcopy,y1,0)

    dendogram += [[y2,y1]]
    return(xcopy)

n = x.shape[0]
while(n > 1):
    x = hclust(x, dendogram, n)
    n = (x.shape[0])
print(dendogram)

