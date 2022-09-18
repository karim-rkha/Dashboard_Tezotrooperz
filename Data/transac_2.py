from urllib import response
import requests 
import json
import pickle
import pandas as pd
from datetime import date
from datetime import datetime
from dateutil import parser
import random


with open("keepers", "rb") as fp:   # Unpickling
    a1_keepers = pickle.load(fp)


with open("a1_minters", "rb") as fp:   # Unpickling
    a1_minters = pickle.load(fp)

with open("dropers", "rb") as fp:   # Unpickling
    sellers = pickle.load(fp)

with open("a2_minters", "rb") as fp:   # Unpickling
    a2_minters = pickle.load(fp)


random.shuffle(a1_minters)





def nft_info(ad):
    response=requests.get(f"https://api.tzkt.io/v1/tokens/balances?account={ad}&token.standard=fa2&firstTime.lt=2022-02-15&limit={10000}").json()
    nb_of_nfts=0
    nb_buy=len(response)
    nb_sell=len(response)
    doga_inter=0
    days_bf_fst=None
    if len(response)>0:
        firstTime=response[0].get("firstTime")[:10]
        days_bf_fst=(datetime(2022, 2, 15)-parser.parse(firstTime)).days
        for res in response:
            balance=int(res.get("balance"))
            lastTime=res.get("lastTime")[:10]
            # print(res)
            # Calculating number of NFTs
            if balance>0 or parser.parse(lastTime) > datetime(2022, 2, 15):
                nb_of_nfts+=1
            contract_address=res.get("token").get("contract").get("address")
            # print(contract_address)
            if contract_address=="KT1NVvPsNDChrLRH5K2cy6Sc9r1uuUwdiZQd":
                doga_inter+=1

    nb_sell=nb_buy-nb_of_nfts
    


    return {'nb_of_nfts':nb_of_nfts,'nb_buy':nb_buy, 'nb_sell':nb_sell, 'doga_inter':doga_inter, 'days_bf_fst':days_bf_fst}


def transac_info(ad):
    response=requests.get(f"https://api.tzkt.io/v1/accounts/{ad}/operations?limit={1000}&timestamp.lt=2022-02-15").json()
    nb_tsc=0
    fst_seen=None
    lst_seen=None
    nb_sent=0
    nb_rec=0
    tot_gas=0
    avg_gas=0
    doga_staking=0
    if len(response)>0:
        firstTime=response[-1].get("timestamp")[:10]
        fst_seen=(datetime(2022, 2, 15)-parser.parse(firstTime)).days

        lastTime=response[0].get("timestamp")[:10]
        lst_seen=(datetime(2022, 2, 15)-parser.parse(lastTime)).days
        for res in response:
            type=res.get("type")
            if type == "transaction":
                nb_tsc+=1
                sender=res.get("sender").get("address")
                receiver=res.get("target").get("address")
                if sender==ad:
                    nb_sent+=1
                if receiver == ad:
                    nb_rec+=1
                tot_gas+=res.get("gasUsed")

                if sender == "KT1EF89rHUm71YoFqUTnc4DjiPUas9HyGWb1" or receiver == "KT1EF89rHUm71YoFqUTnc4DjiPUas9HyGWb1":
                    doga_staking+=1
        avg_gas=int(tot_gas/nb_tsc)
    return {'nb_tsc':nb_tsc,'nb_sent':nb_sent, 'nb_rec':nb_rec, 'fst_seen':fst_seen,'lst_seen':lst_seen,'tot_gas':tot_gas,'avg_gas':avg_gas,'doga_staking':doga_staking}

def make_df(addresses):
    df = pd.DataFrame()
    i=0
    for ad in addresses:
        print(i)
        address={'address':ad}
        nft=nft_info(ad)
        tsc=transac_info(ad)
        if ad in a1_keepers:
            keepers={"keeper":1}
        else:
            keepers={"keeper":0}
        print(keepers)
        add={**address,**nft, **tsc,**keepers}
        df=df.append(add, ignore_index = True)

        i+=1

    return df


# df=make_df(a1_minters[:10])
# print(df.columns)
# print(df.head(10))

with open("df_a1to2", "wb") as fp:  # Pickling
        pickle.dump(make_df(a1_minters), fp)
