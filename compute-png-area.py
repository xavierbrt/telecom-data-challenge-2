import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import cv2

ROOT = "./" #"drive/My Drive/Colab Notebooks/Data Challenge 2/"
RANDOM_STATE = 261





res = []
for i in range(2511):
    im = cv2.imread(ROOT + "data-display/xtest/" + str(i) + ".png", cv2.IMREAD_GRAYSCALE)
    im = np.where(im == 255, 0, im) 
    im = np.where(im > 0, 1, im) 
    res.append(np.sum(im) / (800*1600))
    print(i)

print(len(res))
df_res = pd.DataFrame(res, columns=["res"])
df_res.to_csv(ROOT + "xtest_surfaces.csv", sep=",", index=False)

