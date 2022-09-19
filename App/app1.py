import yfinance as yf
import streamlit as st
from datetime import datetime, timedelta
import pickle
import plotly.express as px
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")



with open("df", "rb") as fp:   # Unpickling
    df = pickle.load(fp)

header = st.container()
conversion_data = st.container()
score = st.container()



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



def select_f(dataset,select):
    if select == "All":
        return dataset
    if select == "Score = 0":
        dataset_bis=dataset.loc[dataset['Score'] == 0]
        return dataset_bis
    if select == "Score ≤ 10":
        dataset_bis=dataset.loc[dataset['Score'] <= 10]
        return dataset_bis
    if select == "Score ≤ 25":
        dataset_bis=dataset.loc[dataset['Score'] <= 25]
        return dataset_bis
    if select == "Score ≤ 50":
        dataset_bis=dataset.loc[dataset['Score'] <= 50]
        return dataset_bis

    if select == "Score ≥ 50":
        dataset_bis=dataset.loc[dataset['Score'] >= 50]
        return dataset_bis
    if select == "Score ≥ 75":
        dataset_bis=dataset.loc[dataset['Score'] >= 75]
        return dataset_bis
    if select == "Score ≥ 90":
        dataset_bis=dataset.loc[dataset['Score'] >= 90]
        return dataset_bis


with header:
    st.title("Datcom X Tezotrooperz")


with conversion_data:
    h_col1, h_col2 = st.columns(2)

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



with score:

    uploaded_file = st.file_uploader("Upload CSV", type=".csv")

    use_example_file = st.checkbox(
        "Use example file", True, help="Score of sample dataset of Tezotrooperz WL wallets"
    )

    if use_example_file:
        select_df = st.selectbox("Select Score : ", options=["All","Score = 0","Score ≤ 10",
                                                                   "Score ≤ 25", "Score ≤ 50", "Score ≥ 50", "Score ≥ 75", "Score ≥ 90"], index=0, key='select_df')

        with open("example_df", "rb") as fp:   # Unpickling
            example_df = pickle.load(fp)
        
        example_df=select_f(example_df,select_df)
        
        fig = go.Figure(data=[go.Table(
        header=dict(values=list(example_df.columns),
                    fill_color='#CCE5E7',
                    align='left'),
        cells=dict(values=[example_df['Wallet'], example_df['Score']],
                fill_color='#F4F3F3',
                align='left'))
                ])
        
        fig.update_layout(
        autosize=False,
        # width=900,
        height=700)

        st.plotly_chart(fig,use_container_width = True)

        def convert_df(data):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return data.to_csv().encode('utf-8')
        

        csv = convert_df(example_df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Datcom_Example_File.csv',
            mime='text/csv',
        )

        


    else:
        st.text("")
        st.text("To get score your community, send a file to : karimrkha@gmail.com :)")
    
    
