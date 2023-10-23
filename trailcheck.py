import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib as plt
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Superstore!!!", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart: Sample SuperStore EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
# from util import same_timestamp
tab1, tab2 = st.tabs(["Data", "Charts"])
with tab1:
  #Uploading the data 
  df= pd.read_csv(r"Superstore.csv", header=0,encoding='latin-1')
  st.write(df)
  
  #MultiSelect Widget( Takes more than 1 Input)
  market=st.sidebar.multiselect(label='Market',options=df['Market'].unique(),default=df['Market'].unique())
  df=df[df["Market"].isin(market)] #Updating the Dataframe
  st.header("Data After Market Filter")
  st.write(df)
  with st.expander("Market_ViewData"):
    csv = df.to_csv(index = False)
    st.download_button("Download Data", data = csv, file_name = "Market.csv", mime = "text/csv",
                       help = 'Click here to download the data as a CSV file')
  
  #SelectBox Widget( Takes only 1 Input)
  cat=st.sidebar.selectbox(label='Category',options=df['Category'].unique())
  df=df[df["Category"]==cat]
  st.header("Data After Category Filter") 
  st.write(df)
  
  #Converting Object into Datetime.date 
  df["Order Date"] = pd.to_datetime(df["Order Date"]).dt.date
  df["Ship Date"] = pd.to_datetime(df["Ship Date"]).dt.date
  
  startDate,endDate = df["Order Date"].min(),df["Order Date"].max()
  df=df.sort_values(['Order Date'])
  
  #Slider Widget (Takes a range)
  chosen_dates = st.sidebar.slider(label='Date Slider', min_value=startDate, max_value=endDate, value=(startDate, endDate), format="YYYY/MM/DD")
  df = df.loc[(df['Order Date']>=chosen_dates[0]) & (df['Order Date']<=chosen_dates[1]), :]
  st.header("Data After Date Slider")
  st.write(df)
  
  #converting datetime.date to datetime and adding new Monthly level date variable
  df["Order Date"]=pd.to_datetime(df["Order Date"])
  df["month_year"] = df["Order Date"].dt.to_period("M")

with tab2:
#Linechart using Ploty
  st.header("Line Chart ")
  linecharteq = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
  # linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
  linechart= linecharteq[['Sales','month_year']]
  st.line_chart(linechart,x="month_year", y="Sales", color=None, width=1000, height=500, use_container_width=True)
  
  st.header("line Chart two")
  linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
  fig2 = px.line(linechart, x = "month_year", y="Sales", labels = {"Sales": "Sales"},height=500, width = 1000,template="gridon")
  st.plotly_chart(fig2,use_container_width=True) 
  
