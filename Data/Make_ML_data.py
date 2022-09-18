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

# col=[]
# for tuple in sort_WL_Minters:
#     col.append(tuple[0])
col=['Wallets','Minter','Tezotopia Resources','GIF DAO', 'Diplomat NFTs', 'Tezotopia NFT Registry', 'Rocket Monsters', 'Tezzles', 'FLAME', 'Tezos Degen Club', 'Froggos', 'VesselsGen0', 'Mekatron K9', 'Fellowship of Ilmeresh', 'Oxtazy', 'crDAO', 'PXL', 'PandaCoin', 'WRAP Governance Token', 'DOGAMÍ NFTs', 'Wrapped Tokens Contract', 'PixelDebates Tokens', 'PixelPotus 1.0', 'DOGAMÍ Doga Bones', 'CRUNCH', 'GAP Threads Asset Manager', 'Chop Sumo', 'Bunny Knights 2nd Gen', 'QUIPU', 'Pixel Panda', 'Youves Synthetic Asset', 'WTZ', 'OWLZ', 'Mooncakes', 'SPI', 'Minterpop Multi Asset Manager 2', 'Atelier 09', 'SpacePunky', 'Salsa', 'Papa Johns Hot Bags', 'KALAM', 'TezApeGang', 'pxlDAO', 'CUBE HEAD collaborations', 'Codename: AK1RA', 'WALLY and his Wonderful Wardrobe', 'PixelPotus 2.0', 'Flux Tribe', 'Tezzles Tributes', 'Kalamint Art House', 'Minterpop Multi Asset Manager 1', 'tzDropz', 'YOU Governance', 'sCasino Tokens', 'Materia', 'hDAO', 'Peace for Ukraine', 'TezDAO', 'FXHASH GENTK', 'PixelPotus Founders Edition', 'CR7 - TezoTrooperz Tribute', 'Ottez Extras', 'Ottez Oysters', 'Tezos Domains NameRegistry', 'Rarible', 'Ottez', 'akaSwap NFTs', 'hic et nunc NFTs', None, 'CyberKidz Club', 'Unibotz Collectables', 'Les Éléfants Terribles', 'Tezos Thugs', 'Versum Items', 'Ziggurats', 'Cyber Gecko Gang', 'GOGOs', 'The Moments', 'NEONZ', 'PRJKTNEON Token', 'Tezzardz', 'Lightfields', '8bidou 8x8', 'Skeletons, Etc.', 'Randomly Common Skeles']

df = pd.DataFrame(columns=col)




i=0
for w in WL:
    l=[w]
    if w in minters:
        l.append(1)
    else:
        l.append(0)
    j=0
    for c in col:
        if j>1:
            if c in inv_WL[w]:
                l.append(1)
            else:
                l.append(0)
        j+=1
    df.loc[i]=l
    i+=1

# for x in d:
#     name=col[i]
#     if res_WL[name]>=3:
#         df.loc[i+1] = [name,len(d[name]['WL']),str(res_WL[name])+"%",str(res_WL_Minters[name])+"%",len(d[name]['WL_Minters'])]
#     i+=1

# print(df.head())


with open("/Users/rkhachahamkarim/Documents/GitHub/Dashboard_Tezotrooperz/App/ml_df", "wb") as fp:  # Pickling
    pickle.dump(df, fp)










