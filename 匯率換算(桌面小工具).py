import pandas as pd
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Exchange Rate')
window.geometry('1000x400')
window.configure(background='#FFF8DC')

text_label = tk.Label(window,text = '外幣兌台幣匯率換算')
text_label.config(font=('Arial',44,),fg='#DAA520',bg='#FFF8DC')
text_label.pack()

input_frame = tk.Frame(window)
input_frame.config(bg='#FFF8DC')
input_frame.pack(side=tk.TOP)
input_label = tk.Label(input_frame,text='輸入兌換金額')
input_label.config(font=('Arial',20),bg='#FFF8DC')
input_label.pack(side='left', ipadx=20, padx=30)
input_entry = tk.Entry(input_frame,width=20)
input_entry.config(font=('Arial',20))
input_entry.pack(side='right', ipadx=20, padx=30)

currency = {
    'unit':['美金USD','日幣JPY','英鎊GBP'],
    'data':[29.79, 0.2801, 39.5]
    }
df = pd.DataFrame(currency, index=currency['unit'])

input_currency = tk.Frame(window)
input_currency.config(bg='#FFF8DC')
input_currency.pack(side=tk.TOP)
currency_label = tk.Label(input_currency,text='選擇幣別')
currency_label.config(font=('Arial',20),bg='#FFF8DC')
currency_label.pack(side='left', ipadx=35, padx=30)
select_currency = ttk.Combobox(input_currency,values=currency['unit'],width=15)
select_currency.config(font=('Arial',20))
select_currency.pack(side='right', ipadx=35, padx=20)

result_label = tk.Label(text='**** \t新台幣NTD')
result_label.config(font=('Arial',20),fg='#B8860B',bg='#FFF8DC')
result_label.pack()


def exchange_rates():
    input_value = float(input_entry.get())
    input_unit = float(df.loc[select_currency.get(),'data'])
    value_unit = input_value *input_unit

    result_label.configure(text= str(value_unit) + '新台幣NTD')

button = tk.Button(window,text='exchange rates',command=exchange_rates)
button.config(font=('Arial',20))
button.pack()

window.mainloop()