import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

ROOT = "./" #"drive/My Drive/Colab Notebooks/Data Challenge 2/"
RANDOM_STATE = 261

if len(sys.argv) < 2:
    print("No submission number given as argument")
    exit()



result = np.loadtxt(ROOT + 'submissions/submission_' + sys.argv[1] + '.csv', delimiter= ' ')
df_res = pd.DataFrame()
df_res["index"] = np.argsort(-result)
df_res["score"] = -np.sort(-result)

"""score_str = str(round(df_res["score"][0], 4)).replace(".", ",")
print(score_str)
print(type(df_res["score"][0]))"""


for i in range(df_res.shape[0]):
    score_str = str(round(df_res["score"][i], 4)).replace(".", ",")
    # We add decimals if there are less than 4 decimals (impotant for the sorting order of the files on Ubuntu file explorer)
    while len(score_str.split(',')[1]) < 4:
        score_str += "0" 

    src = ROOT + 'submissions/' + sys.argv[1] + '/' + str(df_res["index"][i]) + '.png'
    dest = ROOT + 'submissions/' + sys.argv[1] + '/' + score_str + " - " + str(df_res["index"][i]) + '.png'
    os.rename(src, dest)
    print(i)


