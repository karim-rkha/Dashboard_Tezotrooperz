import requests
import json
import pickle
import pandas as pd
import random
from datetime import datetime
from dateutil import parser


with open("tz_holders", "rb") as fp:   # Unpickling
    holders = pickle.load(fp)


with open("WL_bis", "rb") as fp:   # Unpickling
    WL = pickle.load(fp)

def NI(who):  # Nfts held
    i = 1
    nft = {}
    inv = {}
    for him in who:
        response = requests.get(
            f"https://api.tzkt.io/v1/tokens/balances?token.standard=fa2&account={him}&balance.ne=0&limit={10000}").json()
        nft[him] = len(response)
        inv[him] = []
        for res in response:
            inv[him].append(res.get("token").get("contract").get("alias"))
        print(i)
        i += 1
        print(him, "holds ", nft[him], "NFTs")
        # print("And invested in ",inv[him])

    return [nft, inv]

with open("NI_WL", "wb") as fp:  # Pickling
    pickle.dump(NI(WL), fp)



with open("NI_WL", "wb") as fp:  # Pickling
    pickle.dump(NI(WL), fp)


def NI(who):  # Nfts held
    i = 1
    inv = {}
    for him in who:
        response = requests.get(
            f"https://api.tzkt.io/v1/tokens/balances?token.standard=fa2&account={him}&firstTime.le=2022-04-05&limit={10000}").json()
        inv[him] = []
        for res in response:
            balance = int(res.get("balance"))
            lastTime = res.get("lastTime")[:10]
            if balance > 0 or parser.parse(lastTime) > datetime(2022, 4, 5):
                alias = res.get("token").get("contract").get("alias")
                inv[him].append(alias)
                print(him, " invested in : ", alias)
        print(i)
        print("")
        i += 1

    return inv


with open("NI_WL_5", "wb") as fp:  # Pickling
    pickle.dump(NI(WL), fp)
