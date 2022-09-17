import yfinance as yf
import streamlit as st
from datetime import datetime, timedelta
import pickle
import plotly.express as px
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go

# st.set_page_config(layout="wide")

# with open("/Users/rkhachahamkarim/Documents/GitHub/Dashboard_Tezotrooperz/Data/WL_bis", "rb") as fp:   # Unpickling
#     WL = pickle.load(fp)

# with open("/Users/rkhachahamkarim/Documents/GitHub/Dashboard_Tezotrooperz/Data/tz_minters", "rb") as fp:   # Unpickling
#     minters = pickle.load(fp)

# with open("/Users/rkhachahamkarim/Documents/GitHub/Dashboard_Tezotrooperz/Data/NI_WL_5_new", "rb") as fp:   # Unpickling
#     inv_WL = pickle.load(fp)

with open("df", "rb") as fp:   # Unpickling
    df = pickle.load(fp)

header = st.container()
conversion_data = st.container()

# d={}
# for ad in inv_WL:
#     for x in inv_WL[ad]:
#         if x not in d:
#             d[x]=[ad]
#         else:
#             if ad not in d[x]:
#                 d[x].append(ad)

# res_WL={}
# for x in d:
#     res_WL[x]=len(d[x])


# sort_inv_bis = sorted(res_WL.items(), key=lambda x: x[1], reverse=True)


# col=['Overall']
# for tuple in sort_inv_bis[:30]:
#     col.append(tuple[0])


# def f_conversion(name):
#     if name == "Overall":
#         count = 0
#         for ad in WL:
#             if ad in minters:
#                 count += 1

#         h_col1.text(str(len(WL))+" wallets were Whitelisted, "+"among them there were "+ str(count)+" minters")
#         h_col2.text("The conversion rate is : "+str(round(100*count/len(WL),2))+"%")

#     else:
#         name_holders = []
#         WL_minters = []
#         for ad in inv_WL:
#             if name in inv_WL[ad]:
#                 name_holders.append(ad)
#                 if ad in minters:
#                     WL_minters.append(ad)

#         h_col1.text(str(round(100*len(name_holders)/len(WL),2))+"% of the WL were "+name+" holders")
#         h_col2.text("The conversion rate is : "+str(round(100*len(WL_minters)/len(name_holders),2))+"%")

with header:
    st.title("Datcom X Tezotrooperz")

#     source_users = st.selectbox("Source of revenue : ", options=col, index=0, key='daily_users')


# with conversion:
#     h_col1, h_col2 = st.columns([2, 1])

#     f_conversion(source_users)


with conversion_data:
    # df=sns.load_dataset("df")
    # st.dataframe(df,2000, 500)
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df['Name'], df['Number of WL spots'], df['Percentage of the WL'], df['Conversion rate'],df['Number of minters']],
               fill_color='lavender',
               align='left'))
            ])

    st.plotly_chart(fig)

