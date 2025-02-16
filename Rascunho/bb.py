import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime

st.set_page_config('Bollinger Bands On Candlestick Chart', layout='wide')
st.sidebar.header('Select Ticker and Date')
today = datetime.date.today()

ticker = st.sidebar.text_input('Ticker', 'AAPL')
st.header('Bollinger Bands of: ' + ticker)
start_date = st.sidebar.text_input('Start Date', '2021-11-27')
end_date = st.sidebar.text_input('Start Date', f'{today}')

start = pd.to_datetime(start_date)
end = pd.to_datetime(end_date)

data = yf.download(ticker, start, end)
st.dataframe(data, width=1800, height=600)

df = pd.DataFrame(data)

df['middle_band'] = df['Close'].rolling(window=20).mean()
df['upper_band'] = df['middle_band'] + 1.96 * df['Close'].rolling(window=20).std()
df['lower_band'] = df['middle_band'] - 1.96 * df['Close'].rolling(window=20).std()

fig = go.Figure(data=[go.Candlestick(x=df.index, open=df.Open, high=df.High, low=df.Low, close=df.Close, name='Candle Stick Chart'),
                      go.Scatter(x=df.index, y=df.middle_band, line=dict(color='orange', width=1), name='Middle Band'),
                      go.Scatter(x=df.index, y=df.upper_band, line=dict(color='blue', width=1), name='Upper Band'),
                      go.Scatter(x=df.index, y=df.lower_band, line=dict(color='blue', width=1), name='Lower Band')
                     ])
fig.update_layout(autosize=True, width=1280, height=800)

st.plotly_chart(fig)
