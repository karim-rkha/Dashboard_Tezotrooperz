import yfinance as yf
import streamlit as st
from datetime import datetime, timedelta
import pickle
import plotly.express as px
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
from matplotlib.figure import Figure

st.set_page_config(layout="wide")

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

def position_name(options):
    df_neww=df
    df_neww['Conversion rate'] = df_neww['Conversion rate'].str.replace('%','')
    df_neww['Conversion rate'] = df_neww['Conversion rate'].astype(float)
    options_bis=[]
    conv={}
    for o in options:
        conv[o]=float(df_neww.loc[df['Name']==o]['Conversion rate'])
    sort_conv = sorted(conv.items(), key=lambda x: x[1], reverse=True)

    for tuple in sort_conv:
        options_bis.append(tuple[0])
    return options_bis
    

def df_barplot(names):
    df_new=df
    # st.dataframe(df_new)
    # df_new['Conversion rate'] = df_new['Conversion rate'].str.replace('%','')
    # df_new['Conversion rate'] = df_new['Conversion rate'].astype(float)
    df_barplot=pd.DataFrame(columns=['Name','Rate'])
    i=0
    for name in names:
        df_barplot.loc[i] = [name,df_new.loc[df['Name']==name]['Conversion rate']]
        i+=1
    df_barplot['Rate'] = df_barplot['Rate'].astype(float)
    return df_barplot



with header:
    st.title("Datcom X Tezotrooperz")

#     source_users = st.selectbox("Source of revenue : ", options=col, index=0, key='daily_users')


# with conversion:
#     h_col1, h_col2 = st.columns([2, 1])

#     f_conversion(source_users)


with conversion_data:
    h_col1, h_col2 = st.columns(2)

    options = h_col1.multiselect(
    'Select NFT collection',
    list(df['Name']),
    ['Tezotopia Resources','Overall','Randomly Common Skeles'])

    options=position_name(options)
    df_b=df_barplot(options)

    fig = Figure()
    # fig.set_figheight(5)
    # fig.set_figwidth(15)
    ax = fig.subplots()
    sns.barplot(x=df_b['Name'], y=df_b['Rate'], color="goldenrod", ax=ax)
    overall_conversion=float(df.loc[df['Name']=='Overall']['Conversion rate'])
    for bar in ax.patches:
        if bar.get_height() >= overall_conversion:
            if bar.get_height() == overall_conversion:
                bar.set_color('#acd0d3')  
            else:
                bar.set_color('#c8694b')
            # bar.set_color('#1B9ED3')  
          
        else:
            bar.set_color('#e7e7e7')
    # ax.set_xticklabels(rotation=90)
    ax.tick_params(labelrotation=90)
    ax.set_ylabel("Conversion rate")
    ax.set_xlabel("NFT collection")

    h_col1.pyplot(fig)


    # df=sns.load_dataset("df")
    # st.dataframe(df,2000, 500)



    # fig, ax = plt.subplots(figsize=(width, height))
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='#CCE5E7',
                align='left'),
    cells=dict(values=[df['Name'], df['Number of WL spots'], df['Percentage of the WL'], df['Conversion rate'],df['Number of minters']],
               fill_color='#F4F3F3',
               align='left'))
            ])
    
    fig.update_layout(
    autosize=False,
    width=700,
    height=600)

    h_col2.plotly_chart(fig)