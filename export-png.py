import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.neighbors import LocalOutlierFactor
import time
import gc

ROOT = "./" #"drive/My Drive/Colab Notebooks/Data Challenge 2/"
RANDOM_STATE = 261

from scipy.signal import lfilter

n = 1000  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1



"""
print("Load xtrain")
xtrain = np.loadtxt(ROOT + 'data/airbus_train.csv', delimiter= ' ') #, max_rows=1000)
print("Train:", xtrain.shape)
print("xtrain loaded")


for i in range(xtrain.shape[0]):
    xtrain[i] =  lfilter(b, a, xtrain[i,:])
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(xtrain[i,1000:-1000])
    fig.savefig(ROOT + "data-display/xtrain_rolling/" + str(i))
    ax.cla()
    fig.clf()
    plt.close(fig)
    gc.collect()
    print(i)

del xtrain
"""

print("Load xtest")
xtest = np.loadtxt(ROOT + 'data/airbus_test.csv', delimiter= ' ', max_rows=1000) #skiprows=1000)
print("Test:", xtest.shape)
print("xtest loaded")

for i in range(0, xtest.shape[0]):
    xtest[i] =  lfilter(b, a, xtest[i,:])
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(xtest[i,1000:-1000])
    fig.savefig(ROOT + "data-display/xtest_rolling/" + str(i)) #+1000))
    ax.cla()
    fig.clf()
    plt.close(fig)
    gc.collect()
    print(i)

