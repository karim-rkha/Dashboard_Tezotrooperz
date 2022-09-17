import requests
import json
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


with open("NI_WL", "rb") as fp:   # Unpickling
    inv_bis = pickle.load(fp)[1]
with open("WL_bis", "rb") as fp:   # Unpickling
    WL = pickle.load(fp)

d={}
for ad in inv_bis:
    for x in inv_bis[ad]:
        if x not in d:
            d[x]=[ad]
        else:
            if ad not in d[x]:
                d[x].append(ad)

inv={}
for x in d:
    inv[x]=len(d[x])

l=[]
for x in d:
    l=l+d[x]

print(len(list(set(l))))

# print(len(list(set(WL))))

# print(Counter(WL))
    
# print(len(list(set(l))))
# sort_inv = sorted(inv.items(), key=lambda x: x[1], reverse=True)


# print(sort_inv.pop(0))
# print(sort_inv.pop(0))
# print(sort_inv.pop(0))
# print(sort_inv.pop(2))
# print(sort_inv.pop(4))
# # print(sort_inv.pop(1))
# # print(sort_inv.pop(4))
# # print(sort_inv.pop(7))
# # print(sort_inv.pop(9))

# nft=[]
# occ=[]
# for i in sort_inv[:10]:
#     nft.append(i[0])
#     occ.append(i[1])
#     print(i[0], i[1])
