import requests
import json
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


with open("NI_WL_5_new", "rb") as fp:   # Unpickling
    inv_WL = pickle.load(fp)

with open("NI_minters_5_new", "rb") as fp:   # Unpickling
    inv_minters = pickle.load(fp)

with open("WL_bis", "rb") as fp:   # Unpickling
    WL = pickle.load(fp)

d={}
for ad in inv_minters:
    for x in inv_minters[ad]:
        if x not in d:
            d[x]=[ad]
        else:
            if ad not in d[x]:
                d[x].append(ad)

res_minters={}
for x in d:
    res_minters[x]=len(d[x])

# str(round(100*len(d[x])/len(inv_bis),2))+"%"


sort_inv = sorted(res_minters.items(), key=lambda x: x[1], reverse=True)


print(len(inv_minters))
for tuple in sort_inv[:30]:
    print(tuple[0]," : ",str(round(100*tuple[1]/len(inv_minters),2))+"%")


# print(sort_inv[:30])
print("")
print("")


d={}
for ad in inv_WL:
    for x in inv_WL[ad]:
        if x not in d:
            d[x]=[ad]
        else:
            if ad not in d[x]:
                d[x].append(ad)

res_WL={}
for x in d:
    res_WL[x]=len(d[x])


sort_inv_bis = sorted(res_WL.items(), key=lambda x: x[1], reverse=True)



print(len(inv_WL))
for tuple in sort_inv_bis[:30]:
    print(tuple[0]," : ",str(round(100*tuple[1]/len(inv_WL),2))+"%")



print("")
print("")


# print("test")
d={}
for tuple in sort_inv_bis:
    if tuple[0]in res_minters:
        d[tuple[0]] = round(100*abs(res_minters[tuple[0]]/len(inv_minters) -res_WL[tuple[0]]/len(inv_WL)),2)

# print("test")
sort_inv = sorted(d.items(), key=lambda x: x[1], reverse=True)


# print("test")
# print(sort_inv[:30])
for tuple in sort_inv[:30]:
    print(tuple[0]," : ",tuple[1])


