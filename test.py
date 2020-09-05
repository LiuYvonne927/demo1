import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import time

url = 'https://www.findrate.tw/bank/29/#.XwlxJ20zapo'
headers = {'user-angent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
res =  requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.text
soup = BeautifulSoup(html, 'html.parser')
performance_list = []
for index in range(2,21):
    performance_dist = {}
    
    performance_dist['unit_data'] = soup.select(f'#right > table:nth-child(9) > tbody > tr:nth-child({index}) > td.flag > a')[0].text
    performance_dist['unit_price'] = soup.select(f'#right > table:nth-child(9) > tbody > tr:nth-child({index}) > td:nth-child(3)')[0].text
    performance_list.append(performance_dist)
    print( performance_dist)

headers= ['unit_data','unit_price']
with open('performance.csv','w',encoding='utf-8') as output_file:
  dict_writer = csv.DictWriter(output_file,headers)
  dict_writer.writeheader()
  dict_writer.writerows(performance_list)

  

time.sleep(60)