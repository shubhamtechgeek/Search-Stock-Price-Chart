import yfinance as yf
import streamlit as st

st.write(""" # Search Stock Price & Chart! """)
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
user_input = st.text_input("Enter Stock Symbol")
# get data on this ticker
tickerData = yf.Ticker(user_input)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-3-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write(""" ## Closing Price """)
st.line_chart(tickerDf.Close)
st.write(""" ## Volume """)
st.line_chart(tickerDf.Volume)
# show actions (dividends, splits)
st.write("""### Enter Stock Symbol to get info """)
tickerData.info
