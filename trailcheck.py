import streamlit as st
df= pd.read_csv(r"Superstore.csv", header=0,encoding='latin-1')
st.write(df)
st.write("Trail test 1")
