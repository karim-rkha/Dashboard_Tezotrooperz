from unittest import result
import requests
import json
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import parser
import seaborn
from collections import Counter


with open("WL_bis", "rb") as fp:   # Unpickling
    WL = pickle.load(fp)


with open("NI_WL_5_new", "rb") as fp:   # Unpickling
    inv_WL = pickle.load(fp)


count =0
WL=[]
for ad in inv_WL:
    WL.append(ad)
    if "Mekatron K9" in inv_WL[ad]:
        count+=1

print(len(list(set(WL))))
print(count)








