import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv("stocks_data.csv", index_col=0, parse_dates=True)
returns = pd.read_csv("returns_data.csv", index_col=0, parse_dates=True)

st.title("📈 Stock Analysis Dashboard")
stock = st.sidebar.selectbox("Choose a stock", data.columns)

fig = px.line(data, x=data.index, y=stock, title=f"{stock} Stock Price")
st.plotly_chart(fig)

st.subheader(f"Daily Returns - {stock}")
fig2 = px.histogram(returns, x=stock, nbins=100, title=f"{stock} Daily Returns Distribution")
st.plotly_chart(fig2)

st.subheader("Correlation Heatmap")
corr = returns.corr()
fig3 = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r")
st.plotly_chart(fig3)
