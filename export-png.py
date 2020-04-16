import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.neighbors import LocalOutlierFactor
import time
import gc

ROOT = "./" #"drive/My Drive/Colab Notebooks/Data Challenge 2/"
RANDOM_STATE = 261
"""
print("Load xtrain")
xtrain = np.loadtxt(ROOT + 'data/airbus_train.csv', delimiter= ' ')
print("Train:", xtrain.shape)
print("xtrain loaded")

for i in range(0, 758):
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(xtrain[i,:])
    fig.savefig(ROOT + "data-display/xtrain/" + str(i))
    ax.cla()
    fig.clf()
    plt.close(fig)
    gc.collect()
    print(i)

del xtrain
"""

print("Load xtest")
xtest = np.loadtxt(ROOT + 'data/airbus_test.csv', delimiter= ' ', skiprows=1000)
print("Test:", xtest.shape)
print("xtest loaded")

for i in range(0, xtest.shape[0]):
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(xtest[i,:])
    fig.savefig(ROOT + "data-display/xtest/" + str(i+1000))
    ax.cla()
    fig.clf()
    plt.close(fig)
    gc.collect()
    print(i)