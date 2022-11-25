import pandas as pd
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")
st.subheader("HI,I am Abhinav :wave:")
st.title("rit student")
st.title("Ramaiah Institute of Technology,550054")
st.subheader("STUDENT")
st.subheader("ABHINAV B M")
st.text("course registratio CIE and attendence Status")
st.subheader("UHV38")
st.subheader("CY32")
st.subheader("CY33")
st.subheader("CY36")
data={
  "Home":[x for x in range(1,11)],
  "Proctorship":[x**2 for x in range(1,11)],
  "Fee":[x for x in range(1,11)],
  "Time table":[x for x in range(1,11)],
  "logout":[x for x in range(1,11)]
}

df = pd.DataFrame(data =data)
col=st.sidebar.selectbox("Select  a column ",df.column)
plt.plot(df['num'],df[col])
st.header('st.button')
st.pyplot
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
