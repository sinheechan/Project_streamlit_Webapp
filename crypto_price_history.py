import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px
from datetime import datetime, timedelta

st.write('# 비트코인 BTC 데이터')

# https://coinmarketcap.com
# scraper = CmcScraper('BTC', '01-01-2021', '07-01-2021') # '%d-%m-%Y'

# Date
current_date = datetime.now().strftime('%d-%m-%Y') # 현재 날짜
seven_days_ago = (datetime.now() - timedelta(days=7)).strftime('%d-%m-%Y') 
scraper = CmcScraper('BTC', seven_days_ago, current_date)

df = scraper.get_dataframe()

fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='7일 간 가격 분석 자료입니다.')
fig_volume = px.line(df, x='Date', y=['Volume'], title='거래량')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)