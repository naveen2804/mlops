import datetime
import pandas as pd
import streamlit as st
import yfinance as yf

st.write(
    """
     # Stock Prize Analyzer

     Shown are the stock prizes of XYZ Company

   """
)
ticker_symbol ="AAPL"
ticker_data = yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",
                              start="2019-01-01",
                              end="2023-02-14")

st.write(f"""
        {ticker_symbol}'s stock price info:
""")
st.dataframe(ticker_df)

st.write("""
        ## Daily Closing Prices on Line Chart
""")

st.line_chart(ticker_df.Close)

st.write("""
        ## Daily Volume on Line Chart
""")

st.line_chart(ticker_df.Volume)

col1,col2 = st.columns(2)
with col1:
  st.header("Daily Closing Prices on Line Chart")
  st.line_chart(ticker_df.Close)

with col2:
  st.header("Daily Volume on Line Chart")
  st.line_chart(ticker_df.Volume)

ticker_symbol=st.text_input("Enter stock symbol of company: ")
st.write(f"""
        {ticker_symbol}'s stock price info:
""")
st.dataframe(ticker_df)
ticker_data = yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",
                              start="2019-01-01",
                              end="2023-02-14")
with col1:
  st.header("Daily Closing Prices on Line Chart")
  st.line_chart(ticker_df.Close)

with col2:
  st.header("Daily Volume on Line Chart")
  st.line_chart(ticker_df.Volume)