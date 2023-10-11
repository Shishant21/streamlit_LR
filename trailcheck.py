import streamlit as st
# df= pd.read_csv(r"Superstore.csv", header=0,encoding='latin-1')
# st.write(df)
github_csv_url="https://github.com/Shishant21/streamlit_LR/blob/main/Superstore.csv"
df = pd.read_csv(github_csv_url)
st.write("Trail test 1")
