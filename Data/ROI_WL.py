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
    NI_WL = pickle.load(fp)


# Overall conversion rate
##################################################################################################################################
count = 0
for ad in WL:
    if ad in minters:
        count += 1


print(len(WL), "were Whitelisted")
print("Among them, there were ", count, "minters")
print("Conversion rate : ", round(100*count/len(WL),2), "%")
##################################################################################################################################


print("")


# Conversion rate Ottez 
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Ottez"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Conversion rate Ottez Oysters
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Ottez Oysters"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Conversion rate PixelPotus
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "PixelPotus 2.0"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Conversion rate Dogami
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "DOGAMÍ NFTs"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Conversion rate Tezotopia
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Tezotopia NFT Registry"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Cyber Gecko Gang
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Cyber Gecko Gang"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Tezotopia Resources
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Tezotopia Resources"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Diplomat NFTs
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Diplomat NFTs"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Tezzles
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Tezzles"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Randomly Common Skeles
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Randomly Common Skeles"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Tezos Domains NameRegistry
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Tezos Domains NameRegistry"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Tezos Degen Club
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Tezos Degen Club"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Rocket Monsters
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Rocket Monsters"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# NEONZ
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "NEONZ"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# Mekatron K9
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Mekatron K9"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# 8bidou 8x8
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "8bidou 8x8"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################


print("")


# QuipuSwap uUSD
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "QuipuSwap uUSD"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", round(100*len(name_holders)/len(WL),2), "% of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", round(100*len(WL_minters)/len(name_holders),2), "%")
##################################################################################################################################