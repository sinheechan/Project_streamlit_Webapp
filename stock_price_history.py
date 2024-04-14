import streamlit as st
from pandas_datareader import data as pdr
from datetime import datetime
import yfinance as yf
yf.pdr_override()

st.write('''
# 삼성전자 주식 데이터
마감 가격과 거래량을 차트로 보여줍니다!
''')

start = datetime(2018,1,1)
end = datetime(2019,12,31)

# https://finance.yahoo.com/quote/005930.KS?p=005930.KS
df = pdr.get_data_yahoo('005930.KS', start, end)

st.line_chart(df.Close)
st.line_chart(df.Volume)
