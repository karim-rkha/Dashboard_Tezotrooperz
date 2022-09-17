import requests
import json
import pickle
import pandas as pd
import matplotlib.pyplot as plt


with open("NI_holders_final_bis", "rb") as fp:   # Unpickling
    inv_bis = pickle.load(fp)[1]

inv={}
for ad in inv_bis:
    investments=inv_bis[ad]
    # print(ad," : " ,investments)
    for i in investments:
        if i not in inv:
            inv[i]=1
        else :
            inv[i]+=1


sort_inv = sorted(inv.items(), key=lambda x: x[1], reverse=True)

print(sort_inv.pop(1))
print(sort_inv.pop(0))
print(sort_inv.pop(0))
print(sort_inv.pop(1))
print(sort_inv.pop(4))
print(sort_inv.pop(7))
print(sort_inv.pop(9))

# print("")
# print(sort_inv[:10])
# print("")

nft=[]
occ=[]
for i in sort_inv[:10]:
    nft.append(i[0])
    occ.append(i[1])
    print(i[0], i[1])

print(nft[:5])

fig = plt.figure(figsize = (10, 5))
 
# print(nft) 
# print(occ)

# creating the bar plot
plt.bar(nft, occ, color ='#800020', width = 0.4)
 
plt.xlabel("NFTs", fontsize=0.1)
plt.xticks(rotation=90)
plt.ylabel("Value")
plt.show()