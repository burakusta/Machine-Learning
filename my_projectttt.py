# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:27:29 2024

@author: burak
"""
!pip install yfinance==0.2.4
import json
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# def make_graph(stock_data, revenue_data, stock):
#     fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
#     stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
#     revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
#     fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
#     fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
#     fig.update_xaxes(title_text="Date", row=1, col=1)
#     fig.update_xaxes(title_text="Date", row=2, col=1)
#     fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
#     fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
#     fig.update_layout(showlegend=False,
#     height=900,
#     title=stock,
#     xaxis_rangeslider_visible=True)
#     fig.show()


apple = yf.Ticker("AAPL")
url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
response=requests.get(url)
results = json.loads(response.text) #that is our info 
# import json
# with open('apple.json') as json_file:
#     apple_info = json.load(json_file)
#     # Print the type of data variable    
#     #print("Type:", type(apple_info))
# apple_info
print(results['country'])
apple_share_price_data = apple.history(period="max")
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="High")
apple.dividendss=apple.dividends
apple.dividendss.plot()
non_zero_values = apple_share_price_data[apple_share_price_data['Dividends'] != 0]
X=non_zero_values[["Date"]]
X['Date'] = pd.to_datetime(X['Date'])
X['year'] = X['Date'].dt.year
Y=non_zero_values["Dividends"]
plt.plot(X[['year']].values,Y)
plt.show()


amd = yf.Ticker("AMD")
url2="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
response2=requests.get(url2)
results2 = json.loads(response2.text)
print(results2['country'])
print(results2['sector'])
my_datas=amd.history(period="max")
my_datas.reset_index(inplace=True)
print(my_datas[["Date","Volume"]].head(1))


url3 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url3).text
soup = BeautifulSoup(data, 'html5lib')
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True) 
netflix_dataframe = read_html_pandas_data[0]
#print(netflix_dataframe.head())




url5 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
data5  = requests.get(url5).text
soup5 = BeautifulSoup(data5, 'html5lib')
soup5.find("title").text ###???


amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup5.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close =col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
print(soup5.find("title"))
print(amazon_data.columns)
print(amazon_data["Open"].iloc[-1])







tesla= yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
#tesla_share_price_data.head()
url12="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
data12  = requests.get(url12).text
soup12 = BeautifulSoup(data12, 'html5lib')
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in soup12.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    renevue = col[1].text
    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":renevue}, ignore_index=True)
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].astype(dtype=float)





GameStop=yf.Ticker("GME")
gme_data=GameStop.history(period="max")
gme_data.reset_index(inplace=True)

url_br="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
data_br = requests.get(url_br).text
soup_br = BeautifulSoup(data_br, 'html5lib')
dfs = pd.read_html(url_br)
dfs[0]["GameStop Annual Revenue(Millions of US $).1"]=dfs[0]["GameStop Annual Revenue(Millions of US $).1"].str.replace('$',"").str.replace(',',"")
dfs[0]["GameStop Annual Revenue(Millions of US $).1"] = dfs[0]["GameStop Annual Revenue(Millions of US $).1"].astype(dtype=float)
dfs[0] = dfs[0].rename(columns={
    "GameStop Annual Revenue(Millions of US $)": "Date",
    "GameStop Annual Revenue(Millions of US $).1": "Revenue"
})
gme_revenue=dfs[0]