import tkinter as tk

import random

window = tk.Tk()

window.title('guess number')

window.geometry('800x200')

window.configure(background='white')

text_label = tk.Label(window, text='考考你猜數字遊戲')

text_label.config(font=('Arial', 25), bg='white')
text_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

result_label = tk.Label(text='請輸入一個 1-100 的整數')
result_label.pack()

answer = random.randint(1,100)
def click_me():
    input_number = int(input_entry.get())
    if input_number  > answer:
         result = '答案比較小唷，再猜猜'
    elif input_number  < answer:
        result = '答案比較大唷，再猜猜'
    else:
        result = '恭喜，答對了'

    result_label.configure( text = result )

button = tk.Button(window,text='click me',command=click_me)
button.pack()

window.mainloop()