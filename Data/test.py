import requests
import json
import pickle
import pandas as pd


with open("tz_data", "rb") as fp:   # Unpickling
    tz_data = pickle.load(fp)[3]


hdl = []
for i in tz_data:
    hdl.append(tz_data[i][-1])


tz_holders = list(set(hdl))

mnt = []
for i in tz_data:
    mnt.append(tz_data[i][0])

tz_minters = list(set(mnt))

print(len(tz_holders))
print(len(tz_minters))

# mnt_bis=[]
# for i in tz_data:
#     mnt_bis.append(tz_data[i])
# print(len(list(set(mnt_bis))))

with open("tz_holders", "wb") as fp:  # Pickling
    pickle.dump(tz_holders, fp)

with open("tz_minters", "wb") as fp:  # Pickling
    pickle.dump(tz_minters, fp)
