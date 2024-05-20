import streamlit as st
import pandas as pd
from plot import make_chart

# st.sidebar.image('logo.png', width=110)
st.sidebar.image('logo.png', width=200)
st.sidebar.title('Restaking TTL')

df = pd.read_csv('ttl_all.csv')
df['symbol']=df['symbol'].str.lower()

unique_symbols = tuple(df['symbol'].unique().tolist())

info_slot = st.empty()
info_slot.text("Please select the token")
Metric = st.sidebar.selectbox('Tokens',options= unique_symbols)


if Metric:
    final = df[df['symbol']==Metric]
    final['symbol']=final['symbol'].str.lower()
    
    chart = make_chart(final)
    button =  st.sidebar.button('Give chart')
    if button:
        info_slot.empty()
        st.text((Metric))
        st.plotly_chart(chart,use_container_width=True)
