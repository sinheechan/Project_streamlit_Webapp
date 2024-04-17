import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px
from datetime import datetime

st.write('# Sinheechan_비트코인')

st.sidebar.header('Menu')

name = st.sidebar.selectbox('Name', ['BTC', 'ETH', 'USDT'])

start_date = st.sidebar.date_input('Start date', datetime(2023, 1, 1))
end_date = st.sidebar.date_input('End date', datetime.now().date())

# https://coinmarketcap.com
scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y')) # '%d-%m-%Y'
df = scraper.get_dataframe()

fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='Price')
fig_volume = px.line(df, x='Date', y=['Volume'], title='Volume')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)