import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gc


PATH_XTRAIN = './data/airbus_train.csv'
PATH_XTEST = './data/airbus_test.csv'
PATH_XTRAIN_EXPORT = "./data-display/xtrain/"
PATH_XTEST_EXPORT = "./data-display/xtest/"


print("Load xtrain")
xtrain = np.loadtxt(PATH_XTRAIN, delimiter= ' ')
print("Train:", xtrain.shape)
print("xtrain loaded")

for i in range(xtrain.shape[0]):
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(xtrain[i])
    fig.savefig(PATH_XTRAIN_EXPORT + str(i))
    ax.cla()
    fig.clf()
    plt.close(fig)
    gc.collect()
    print(i)

del xtrain



print("Load xtest (first part)")
xtest = np.loadtxt(PATH_XTEST, delimiter= ' ', max_rows=1000)
print("Test:", xtest.shape)
print("xtest loaded")

for i in range(0, xtest.shape[0]):
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(xtest[i])
    fig.savefig(PATH_XTEST_EXPORT + str(i))
    ax.cla()
    fig.clf()
    plt.close(fig)
    gc.collect()
    print(i)

del xtest



print("Load xtest (second part)")
xtest = np.loadtxt(PATH_XTEST, delimiter= ' ', skiprows=1000)
print("Test:", xtest.shape)
print("xtest loaded")

for i in range(0, xtest.shape[0]):
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(xtest[i])
    fig.savefig(PATH_XTEST_EXPORT + str(i+1000))
    ax.cla()
    fig.clf()
    plt.close(fig)
    gc.collect()
    print(i)

del xtest
