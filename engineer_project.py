# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:42:40 2024

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
url_burak="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

html_page = requests.get(url_burak).text

data1=pd.read_html(html_page)
data1[2].to_csv(r"C:\Users\burak\OneDrive\Masaüstü\datas\burak.csv", mode='w', index=False)



url2="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/INSTRUCTOR.csv"

attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']
df = pd.read_csv(url2,names=attribute_list)
table_name = 'INSTRUCTOR'
conn = sqlite3.connect('STAFF.db')
df.to_sql(table_name, conn, if_exists = 'replace', index =False)

query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
query_statement2 = f"SELECT FNAME FROM {table_name}"
query_output2 = pd.read_sql(query_statement2, conn)
print(query_output2)


query_statement3 = f"SELECT COUNT (*) FROM {table_name}"
query_output3 = pd.read_sql(query_statement3, conn)
print(query_output3)

query_statement4 = f"PRAGMA table_info({table_name})"
table_structure = pd.read_sql(query_statement4, conn)
print("Tablo Yapısı:")
print(table_structure)

data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
conn.close()
