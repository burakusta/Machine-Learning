# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 00:02:00 2024

@author: burak
"""
pip install lxml
pip install html5lib
import nba_api as a
from nba_api.stats.static import teams
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from nba_api.stats.endpoints import leaguegamefinder
import json
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
nba_teams = teams.get_teams()
# def one_dict(list_dict):
#     keys=list_dict[0].keys()
#     out_dict={key:[] for key in keys}
#     for dict_ in list_dict:
#         for key, value in dict_.items():
#             out_dict[key].append(value)
#     return out_dict
nba_team_df=pd.DataFrame(nba_teams)

df_warriors=nba_team_df[nba_team_df['nickname']=='Warriors']
id_warriors=df_warriors[['id']].values[0][0]
game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)


import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(url, "Golden_State.pkl")

games = pd.read_pickle("Golden_State.pkl")
games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()


import os
from PIL import Image
from IPython.display import IFrame
url='https://www.ibm.com/'
r=requests.get(url)
#results = json.loads(r.content)
#dfff=pd.DataFrame(results)
header=r.headers
header['date']
print(header['date'])
print(header['Content-Type'])
print(r.encoding)
print(r.text[0:100])
url2='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r1=requests.get(url2)
print(r1.headers)
# path=os.path.join(os.getcwd(),'image.png')
# with open(path,'wb') as f:
#     f.write(r.content)
# Image.open(path)

#BURAYA EK GELECEK!!!!

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"
soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())
tag_object = soup.title
tag_object1 = soup.h3
h3_tags = soup.find_all('h3')
tag_child = tag_object1.b
parent_tag = tag_child.parent
parent_body=tag_object1.parent
sibling=tag_object1.next_sibling
tag_object2 = tag_object1.find_next_sibling('h3')
attr=tag_child.attrs
print(tag_child["id"])
tag_string = tag_child.string
table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> \
<td>Payload mass</td></tr><tr> <td>1</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td> \
<td>300 kg</td></tr><tr><td>2</td> \
<td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td> \
<td>94 kg</td></tr><tr><td>3</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td> \
<td>80 kg</td></tr></table>"
soup2 = BeautifulSoup(table, 'lxml')
table_rows =soup2.find_all('tr')
list_input = soup2.find_all(href="https://en.wikipedia.org/wiki/Florida")
url1= "http://www.ibm.com"
data1= requests.get(url).text
soup3 = BeautifulSoup(data1, "lxml")
for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))
for link in soup.find_all('img'):  # in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))
url3 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html" 
data3= requests.get(url3).text
soup3 = BeautifulSoup(data3, 'lxml')
table2 = soup3.find('table')
url21 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
tables = pd.read_html(url21)
