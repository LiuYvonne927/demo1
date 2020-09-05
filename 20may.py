import pandas as pd

import matplotlib.pyplot as plt

#避免中文產生亂碼
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"TaipeiSansTCBeta-Regular.ttf") 

stock_data = pd.read_csv('stock_data.csv', encoding='utf-8')

#將屬性是Object，改成數值屬性
stock_data['收盤價'] = pd.to_numeric(stock_data.收盤價, errors='coerce') 

#取前5筆資料
Data = stock_data.head(5)

# y軸
closing_price =(Data['收盤價'])
# x軸
stock_list = float(Data['證券代號'])

plt.plot(stock_list , closing_price)

plt.title('Stock_Data',fontsize = 15, fontweight = 'bold')
plt.xlabel('證券代號',fontweight = 'bold',fontproperties=font)
plt.ylabel('收盤價',fontweight = 'bold',fontproperties=font)

plt.show()
plt.savefig('plot.png')