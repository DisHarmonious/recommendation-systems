import pandas as pd
import numpy as np
import os
from scipy.spatial import distance
from sklearn.metrics.pairwise import cosine_similarity

os.chdir("C:\\Users\\Sim-Laptop-2\\Desktop\\kalder")
dataset=pd.read_csv(r'data.txt', sep=",")
dataset=dataset.iloc[:,1:]
dataset=dataset.T

### CALCULATE DISTANCE BETWEEN TWO POINTS EXAMPLE
'''
### FUNCTION TO TURN ARRAY TO TUPLE
def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a
'''
### a=dataset.iloc[1,:]
### b=dataset.iloc[2,:]
### a=totuple(a)
### b=totuple(b)
### dist=distance.euclidean(a,b)

### CALCULATE COSINE SIMILARITY BETWEEN TWO POINTS EXAMPLE
### a=dataset.iloc[1,:]
### b=dataset.iloc[2,:]
### a=[a]
### b=[b]
### dist=cosine_similarity(a,b)

recommendations=pd.DataFrame()
N=10 #how many recommendations

### TRAIN
for i in range(0, len(dataset)-1):
    a=dataset.iloc[i,:]
    a=[a]
    distances=[]
    for j in range(0,len(dataset)-1):
        b=dataset.iloc[j,:]
        dist=distance.euclidean(a,b)
        distances.append(dist)
    distances=distances[1:] 
    c="rec"+str(i)
    r=np.argsort(distances)
    recommendations[c]=r[0:N]


### DO A RECOMMENDATION
rec_num=184 # get recommendations for item 64
a=recommendations.iloc[:,rec_num]
print("Recommended artists for " + str(dataset.index.values[rec_num]) + str(':'))
for i in range(len(recommendations)-1):
    print(dataset.index.values[a[i]])











