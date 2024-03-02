 !pip install yfinance==0.2.4
import json
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots  
apple = yf.Ticker("AAPL")
apple_share_price_data = apple.history(period="max")
apple_share_price_data.reset_index(inplace=True)
print(apple_share_price_data)
