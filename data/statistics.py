import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby

df = pd.read_csv("python/train.csv")
code_list = df['raw_code'].tolist()
nl_list = df['raw_nl'].tolist()

df = pd.read_csv("python/dev.csv")
code_list.extend(df['raw_code'].tolist())
nl_list.extend(df['raw_nl'].tolist())

df = pd.read_csv("python/test.csv")
code_list.extend(df['raw_code'].tolist())
nl_list.extend(df['raw_nl'].tolist())

code_len_list = [len(str(code).split()) for code in code_list]

def getBili(num, demo_list):
    s = 0
    for i in range(len(demo_list)):
        if(demo_list[i] < num):
            s += 1
    print('<'+str(num)+'比例为'+str(s/len(demo_list)))

from numpy import *

b = mean(code_len_list)
c = median(code_len_list)
counts = np.bincount(code_len_list)
d = np.argmax(counts)
m = np.max(code_len_list)
print('平均值'+str(b))
print('众数'+str(d))
print('中位数'+str(c))
print('MAX'+str(m))

getBili(8,code_len_list)
getBili(16,code_len_list)
getBili(32,code_len_list)
getBili(64,code_len_list)