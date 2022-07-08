import yfinance as yf
import pickle

tsla = yf.Ticker('TSLA')

print(tsla.recommendations['To Grade'].value_counts().keys()[0])

print(tsla.recommendations['To Grade'].value_counts().keys()[1])

with open('/tmp/script.out', 'wb+') as f:
    pickle.dump({'test': 'ok'}, f)
