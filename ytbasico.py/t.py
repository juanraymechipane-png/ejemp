import yfinance as yf
data = yf.download("INTC", start="2023-09-21", end="2023-11-21", interval="1wk")
print(data.head())
data.to_csv("INTC.csv")
Como Descargar Datos De Yahoo Finance A Excel (2025)Divisa en USD
