# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:55:25 2024

@author: burak
"""

import json
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import zipfile
import io
import glob 
import xml.etree.ElementTree as ET 
from datetime import datetime 
import sqlite3
import numpy as np
url="https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
path="./Largest_banks_data.csv"
db_name="Banks.db"
table_name="Largest_banks"

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')
        

def extract(url1):
    data1= pd.DataFrame()
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    for row in data.find_all('tbody')[0].find_all('tr'):
        col = row.find_all('td')
        if len(col)!=0:
                data_dict = {"Bank Name": col[1].find_all('a')[-1].contents[0],
                             'MC_USD_Billion': col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                data1 = pd.concat([data1,df1], ignore_index=True)
    data1['MC_USD_Billion']=data1['MC_USD_Billion'].str.replace('\n',"").str.replace(',',"")
    data1['MC_USD_Billion']=data1['MC_USD_Billion'].astype("float")
    return data1
                



def transform(data):
    exchange_rate = {
    'GBP': 0.73,  # 1 USD = 0.73 GBP
    'EUR': 0.82,  # 1 USD = 0.82 EUR
    'INR': 73.15  # 1 USD = 73.15 INR
}   
    data['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in data['MC_USD_Billion']]
    data['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in data['MC_USD_Billion']]
    data['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in data['MC_USD_Billion']]
    return data

def load_to_csv(data,csv_path1):
    data.to_csv(csv_path1 , index=False)


def load_to_db(data, table_name1,conn1):
    data.to_sql(table_name1, conn1, if_exists = 'replace', index =False)
    
    
def run_query(query_statement1, conn1):   
     print(query_statement1)
     query_output = pd.read_sql(query_statement1, conn1)
     print(query_output)







log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url)

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, path)

log_progress('Data saved to CSV file')

conn=sqlite3.connect(db_name)

log_progress('SQL Connection initiated.')

load_to_db(df,table_name, conn )

log_progress('Data loaded to Database as table. Running the query')

query_statement=f"SELECT * FROM {table_name}" 
query_statement2=f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
query_statement3=f"SELECT \"Bank Name\" from {table_name} LIMIT 5" 

run_query(query_statement, conn)
run_query(query_statement2, conn)
run_query(query_statement3, conn)

log_progress('Process Complete.')

conn.close()

log_progress("Server Connection closed")

