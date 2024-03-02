# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:37:09 2024

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
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = './Countries_by_GDP.csv'
url='https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
def extract(url1):
    data1= pd.DataFrame()
    html_page = requests.get(url1).text
    data = BeautifulSoup(html_page, 'html.parser')
    for row in data.find_all('tbody')[2].find_all('tr'):
            col = row.find_all('td')
            if len(col)!=0:
                if col[0].find('a') is not None and '—' not in col[2]:
                    data_dict = {"Country": col[0].a.contents[0],
                                 "GDP_USD_billion": col[2].contents[0]}
                    df1 = pd.DataFrame(data_dict, index=[0])
                    data1 = pd.concat([data1,df1], ignore_index=True)
    return data1


def transform(data):
    data["GDP_USD_billion"]=data["GDP_USD_billion"].str.replace(',',"")
    data["GDP_USD_billion"]=data["GDP_USD_billion"].astype("float")
    data["GDP_USD_billion"] = round(data.GDP_USD_billion / 1000,2) 
    data.rename(columns={"GDP_USD_billion": 'GDP_USD_billions'}, inplace=True)
    return data


def load_to_csv(data,csv_path1):
    data.to_csv(csv_path1 , index=False)


    
def load_to_db(data, table_name1,conn1):
    data.to_sql(table_name1, conn1, if_exists = 'replace', index =False)


def run_query(query_statement, conn):   
    print(query_statement)
    query_output = pd.read_sql(query_statement, conn)
    print(query_output)

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./etl_project_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')
        
log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url)

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)

log_progress('Data saved to CSV file')

conn = sqlite3.connect('World_Economies.db')

log_progress('SQL Connection initiated.')

load_to_db(df,table_name, conn )

log_progress('Data loaded to Database as table. Running the query')

query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
run_query(query_statement, conn)

log_progress('Process Complete.')

conn.close()

log_progress("Server Connection closed")