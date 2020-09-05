import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname=r'./NotoSansCJK-Black.ttc')

# 讀取 CSV 資料
df = pd.read_csv('stock_data.csv',encoding='utf-8')

# 選取所有列的 date, year_revenue 欄資料
data = df.loc[0:4, ['證券代號', '收盤價']] 
data['收盤價'] = data['收盤價'].astype('float')
# 將 date 設為 index，要當作 X 軸使用
data = data.set_index('證券代號')

print(data)

# 產生 line chart
fig = data.plot(kind='line').get_figure()

# 設定圖表標頭
plt.title('stock performance')

plt.show()
# 儲存成圖片
fig.savefig('plot.png')