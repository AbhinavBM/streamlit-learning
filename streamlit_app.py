import pandas as pd
import streamlit as st
plt.style.use("ggplot")
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")
st.subheader("HI,I am Abhinav :wave:")
st.title("A Data Analyst From Germany")
data={
  "Home":[x for x in range(1,11)],
  "Proctorship":[x**2 for x in range(1,11)],
  "Fee":[x for x in range(1,11)],
  "Time table":[x for x in range(1,11)],
  "logout":[x for x in range(1,11)]
}

df = pd.DataFrame(data =data)
st.sidebar.selectbox("Select  number ",[1,2,3,4,5])
