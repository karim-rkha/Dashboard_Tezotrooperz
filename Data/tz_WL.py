import requests
import json
import pickle
import pandas as pd


df = pd.read_excel("WL.xlsx")
df.to_csv('WL.csv', encoding='utf-8', index=False)

# print(df.iloc[:, 0])



WL=[]
for ad in df.iloc[:, 0]:
    WL.append(ad)

with open("WL_bis", "wb") as fp:  # Pickling
    pickle.dump(WL, fp)


