import streamlit as st
import pandas

st.set_page_config(layout="wide")


st.header("The Best Company")

content="""
Write a comprehensive description of what your company offers. Explain top products and services, why you created them, and how they can help your customers or clients. This helps readers decide if your business actually has what they need. 
It's also a good section to link out to your company website or product pages
"""
st.write(content)

st.subheader("Our Team")

col1,col2,col3=st.columns(3)

df=pandas.read_csv("data.csv")

with col1:
    for index,row in df[:4].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/"+row["image"])

with col3:
    for index,row in df[8:].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/"+row["image"])



