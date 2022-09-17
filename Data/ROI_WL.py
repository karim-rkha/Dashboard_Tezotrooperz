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


with open("WL", "rb") as fp:   # Unpickling
    WL = pickle.load(fp)

with open("tz_minters", "rb") as fp:   # Unpickling
    minters = pickle.load(fp)

with open("tz_holders", "rb") as fp:   # Unpickling
    holders = pickle.load(fp)

with open("NI_WL_5", "rb") as fp:   # Unpickling
    NI_WL = pickle.load(fp)


# Overall conversion rate
##################################################################################################################################
count = 0
for ad in WL:
    if ad in minters:
        count += 1


print(len(WL), "were Whitelisted")
print("Among them, there were ", count, "minters")
print("Conversion rate : ", count/len(WL), "%")
##################################################################################################################################


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


print(len(name_holders),name,"were whitelisted : ", len(name_holders)/len(WL), "of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", 100*len(WL_minters)/len(name_holders), "%")
##################################################################################################################################

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


print(len(name_holders),name,"were whitelisted : ", len(name_holders)/len(WL), "of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", 100*len(WL_minters)/len(name_holders), "%")
##################################################################################################################################

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


print(len(name_holders),name,"were whitelisted : ", len(name_holders)/len(WL), "of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", 100*len(WL_minters)/len(name_holders), "%")
##################################################################################################################################

# Conversion rate Dogami
##################################################################################################################################
name_holders = []
WL_minters = []
for ad in NI_WL:
    name = "Tezotopia NFT Registry"
    if name in NI_WL[ad]:
        name_holders.append(ad)
        if ad in minters:
            WL_minters.append(ad)


print(len(name_holders),name,"were whitelisted : ", len(name_holders)/len(WL), "of the WL")
print("Among them, there are : ", len(WL_minters), "minters")
print("Conversion rate : ", 100*len(WL_minters)/len(name_holders), "%")
##################################################################################################################################
# PixelPotus 2.0
##################################################################################################################################
# dog_holders = []
# dogxtz = []
# for ad in NI_airdrop:
#     dogami = "PixelPotus 2.0"
#     if dogami in NI_airdrop[ad]:
#         dog_holders.append(ad)
#         if ad in doga:
#             dogxtz.append(ad)


# print("DogaBone was airdropped to ", len(list_airdrop))
# print("Among them, there are : ", len(dog_holders), "PixelPotus holders")
# print("Among these ", len(dogxtz), "hold Dogami")
# print("Conversion rate : ", 100*len(dogxtz)/len(dog_holders), "%")
# ##################################################################################################################################


# Parrotz
##################################################################################################################################
# dog_holders = []
# dogxtz = []
# for ad in NI_cr7:
#     dogami = "Parrotz"
#     if dogami in NI_cr7[ad]:
#         dog_holders.append(ad)
#         if ad in holders:
#             dogxtz.append(ad)


# print("CR7 was airdropped to ", len(cr7))
# print("Among them, there are : ", len(dog_holders), "Parrotz holders")
# print("Among these ", len(dogxtz), "hold Parrotzs")
# print("Conversion rate : ", 100*len(dogxtz)/len(dog_holders), "%")
# ##################################################################################################################################


# Small wallets
##################################################################################################################################
# dog_holders = []
# dogxtz = []
# for ad in NI_airdrop:
#     if len(NI_airdrop[ad]) < 3:
#         dog_holders.append(ad)
#         if ad in doga:
#             dogxtz.append(ad)


# print("CR7 was airdropped to ", len(list_airdrop))
# print("Among them, there are : ", len(dog_holders),
#       "wallets that hold 2 NFTs or less")
# print("Among these ", len(dogxtz), "hold Dogami")
# print("Conversion rate : ", 100*len(dogxtz)/len(dog_holders), "%")
# ##################################################################################################################################
