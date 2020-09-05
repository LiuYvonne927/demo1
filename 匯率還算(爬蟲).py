import pandas as pd
import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import csv
import time


window = tk.Tk() # 建立主視窗
window.title('匯率換算')  # 設定視窗標題
window.geometry('1000x400') # 設定視窗大小 1000x400
window.configure(background='#FFF8DC') # 設定背景顏色

text_label = tk.Label(window,text = '外幣兌台幣匯率換算')
# 建立文字 Label 元件
text_label.config(font=('Arial',44,),fg='#DAA520',bg='#FFF8DC') 
# 設定字型、大小、字體顏色及底色
text_label.pack() 
# pack 渲染元件

input_frame = tk.Frame(window)
input_frame.config(bg='#FFF8DC')
input_frame.pack(side=tk.TOP)
input_label = tk.Label(input_frame,text='輸入兌換金額')
input_label.config(font=('Arial',20),bg='#FFF8DC')
input_label.pack(side='left', ipadx=20, padx=30)
input_entry = tk.Entry(input_frame,width=20)
input_entry.config(font=('Arial',20))
input_entry.pack(side='right', ipadx=20, padx=30)


url = 'https://www.findrate.tw/bank/29/#.XwlxJ20zapo'
headers = {'user-angent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
res =  requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.text
soup = BeautifulSoup(html, 'html.parser')
performance_list = []
for n in range(2,21):
    performance_dist = {}
    performance_dist['unit_data'] = soup.select(f'#right > table:nth-child(9) > tbody > tr:nth-child({n}) > td.flag > a')[0].text
    performance_dist['unit_price'] = soup.select(f'#right > table:nth-child(9) > tbody > tr:nth-child({n}) > td:nth-child(3)')[0].text
    performance_list.append(performance_dist)

headers = ['unit_data','unit_price']

with open('performance.csv','w',encoding='utf-8') as output_file:
  dict_writer = csv.DictWriter(output_file,headers)
  dict_writer.writeheader()
  dict_writer.writerows(performance_list)

pd.read_csv('performance.csv',index_col='unit_data').head(0)

df = pd.read_csv('performance.csv', encoding='utf-8')
print(df)
currency = {
'unit' : [df.loc[0: , 'unit_data']],
'price' : [df.loc[0: , 'unit_price']]
}
print(currency)

print('+++++++++++++++++++++++++++++++++++++++++++++++++')
 
input_currency = tk.Frame(window)
input_currency.config(bg='#FFF8DC')
input_currency.pack(side=tk.TOP)
currency_label = tk.Label(input_currency,text='選擇幣別')
currency_label.config(font=('Arial',20),bg='#FFF8DC')
currency_label.pack(side='left', ipadx=35, padx=30)

unit_list = currency['unit']
b = []
print("--------------------------------------")
print(unit_list)
for a in unit_list:
    print(a)
    print('*****************************************')
    for c in a:
        print('+++++++++++++++++++++++++++++++++++')
        print(c)
        b.append(c)

select_currency = ttk.Combobox(input_currency,values=b,width=15)
select_currency.config(font=('Arial',20))
select_currency.pack(side='right', ipadx=35, padx=20)

result_label = tk.Label(text='**** \t新台幣NTD')
result_label.config(font=('Arial',20),fg='#B8860B',bg='#FFF8DC')
result_label.pack()




def exchange_rates():
    input_value = float(input_entry.get())
    input_unit = float(df.loc[select_currency.get(),'data'])
# 取出input值 '換算金額input_value' '換算幣別input_unit'
    value_unit = input_value *input_unit
# 換算公式
    result_label.configure(text= str(value_unit) + '新台幣NTD')
# 顯示在 Label 元件上 
# configure 方法更新按鈕元件屬性值 text 為 clicked!!!
button = tk.Button(window,text='exchange rates',command=exchange_rates)
# 建立按鈕元件（第一個參數放入 window 代表要顯示在哪個區塊），顯示文字為 '開始換算'，command 是當點擊會觸發處理的函式
button.config(font=('Arial',20))
button.pack()

window.mainloop()
# 運行主程式，最後一定要運行 window.mainloop()，讓 window 不斷地重新整理