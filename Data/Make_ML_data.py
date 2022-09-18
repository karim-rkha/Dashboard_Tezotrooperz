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

with open("tz_minters", "rb") as fp:   # Unpickling
    minters = pickle.load(fp)

with open("tz_holders", "rb") as fp:   # Unpickling
    holders = pickle.load(fp)

with open("NI_WL_5_new", "rb") as fp:   # Unpickling
    inv_WL = pickle.load(fp)

d={}
for ad in inv_WL:
    for x in inv_WL[ad]:
        if x not in d:
            d[x]={'WL':[ad],'WL_Minters':[]}
            if ad in minters:
                d[x]['WL_Minters'].append(ad)
        else:
            if ad not in d[x]['WL']:
                d[x]['WL'].append(ad)
                if ad in minters:
                    d[x]['WL_Minters'].append(ad)

res_WL={}
res_WL_Minters={}
for x in d:
    res_WL[x]=round(100*len(d[x]['WL'])/len(WL),2)
    res_WL_Minters[x]=round(100*len(d[x]['WL_Minters'])/len(d[x]['WL']),2)




sort_WL_Minters = sorted(res_WL_Minters.items(), key=lambda x: x[1], reverse=True)

# print(sort_WL_Minters)

col=[]
for tuple in sort_WL_Minters:
    col.append(tuple[0])

df = pd.DataFrame(columns=['Name','Number of WL spots','Percentage of the WL','Conversion rate','Number of minters'])

df.loc[0]=['Overall',2400,'100%','11.21%',len(minters)]




i=0
for x in d:
    name=col[i]
    if res_WL[name]>=1:
        df.loc[i+1] = [name,len(d[name]['WL']),str(res_WL[name])+"%",str(res_WL_Minters[name])+"%",len(d[name]['WL_Minters'])]
    i+=1

print(df)


with open("/Users/rkhachahamkarim/Documents/GitHub/Dashboard_Tezotrooperz/App/df", "wb") as fp:  # Pickling
    pickle.dump(df, fp)










