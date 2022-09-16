import requests
import json
import pickle
import pandas as pd


# Contract of Tezotrooperz NFTs  || 1682 mints
contract1 = "KT1Gg9cdNu3cFUT2UrUZKBSvTRH8N8AsPk2i"


def tz_data():
    date_trans = {}
    dog_mint = {}
    dog_trans = {}
    dog_hdl = {}
    i = 1

    while i < 2001:
        print("TezoTroopers #", i)
        response = requests.get(
            f"https://api.tzkt.io/v1/tokens/transfers?token.contract={contract1}&token.tokenId={i}&limit={10000}").json()
        if len(response) > 0:

            minter = response[0].get("to").get("address")
            dog_mint[i] = minter
            print("Minter is :", minter)
            print("")

            nb_trans = len(response)
            dog_trans[i] = nb_trans
            print("Was transfered :", nb_trans, " times")
            print("")

            dog_hdl[i] = []

            for res in response:

                dog_hdl[i].append(res.get("to").get("address"))

                date = res.get("timestamp")[:10]
                if date not in date_trans:
                    date_trans[date] = 1
                    print("new date is :", date)
                    print("")
                else:
                    date_trans[date] += 1
                    print("+1 for : ", date)
                    print("")

            print("Holders of ", i, " are :", dog_hdl[i])
            print("")
            print("")

        if i % 1000 == 0:
            with open("Tz_inter", "wb") as fp:  # Pickling
                pickle.dump([date_trans, dog_mint, dog_trans, dog_hdl], fp)
        i += 1

    result = [date_trans, dog_mint, dog_trans, dog_hdl]

    return result


with open("tz_data", "wb") as fp:  # Pickling
    pickle.dump(tz_data(), fp)
