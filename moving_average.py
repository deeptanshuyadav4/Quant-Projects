import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'RELIANCE.NS'
data = yf.download(ticker, start='2023-01-01')

data['SMA_20'] = data['Close'].rolling(window=20).mean()

plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Price')
plt.plot(data['SMA_20'], label='20-day SMA', linestyle='--')
plt.title(f'{ticker} Price & Moving Average')
plt.legend()
plt.show()
