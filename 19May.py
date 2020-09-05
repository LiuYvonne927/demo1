import pandas as pd

df = pd.read_csv('ALL_COUNTRY_AMT.CSV', encoding='utf-8')

print(df.info())

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 744 entries, 0 to 743
#Data columns (total 14 columns):
#   Column       Non-Null Count  Dtype  
#---  ------       --------------  -----  
# 0   年月           742 non-null    object 
# 1   國別           740 non-null    object 
# 2   台北市[金額，新台幣]  740 non-null    float64
# 3   台北市[筆數]      740 non-null    float64
# 4   新北市[金額，新台幣]  740 non-null    float64
# 5   新北市[筆數]      740 non-null    float64
# 6   桃園市[金額，新台幣]  740 non-null    float64
# 7   桃園市[筆數]      740 non-null    float64
# 8   台中市[金額，新台幣]  740 non-null    float64
# 9   台中市[筆數]      740 non-null    float64
# 10  台南市[金額，新台幣]  740 non-null    float64
# 11  台南市[筆數]      740 non-null    float64
# 12  高雄市[金額，新台幣]  740 non-null    float64
# 13  高雄市[筆數]      740 non-null    float64
#dtypes: float64(12), object(2)
#memory usage: 81.5+ KB
#None

#取台北市的資料
df_tpe = pd.DataFrame(df,columns=['年月','國別','台北市[金額，新台幣]','台北市[筆數]']) 

#印出後20筆資料
print(df_tpe.tail(20))

#                      年月   國別  台北市[金額，新台幣]    台北#市[筆數]
#724              109年01月   荷蘭  454545526.0   914991.0
#725              109年01月  新加坡  324847007.0    70858.0
#726              109年01月   香港  230248932.0    83601.0
#727              109年01月   南韓  137058716.0    41945.0
#728              109年01月   法國  202039230.0    16519.0
#729              109年01月  西班牙  146406286.0    17039.0
#730              109年02月   美國  925994207.0   480931.0
#731              109年02月   日本  663748909.0   224842.0
#732              109年02月  愛爾蘭  449715911.0   437189.0
#733              109年02月   荷蘭  459261360.0  1049698.0
#734              109年02月   英國  428616667.0   114697.0
#735              109年02月  新加坡  275604137.0    77424.0
#736              109年02月   澳洲  187283530.0    25645.0
#737              109年02月   南韓   74494474.0    25638.0
#738              109年02月   法國  134882393.0    13128.0
#739              109年02月   香港  102576276.0    81481.0
#740                  NaN  NaN          NaN        NaN
#741                  NaN  NaN          NaN        NaN
#742                  備註1  NaN          NaN        NaN
#743  上述國家別順序係依當月消費金額作排名。  NaN          NaN        NaN

#取109年2月資料
df_tpe_10902 = df_tpe.loc[730:739, ]

print(df_tpe_10902,df_tpe_10902.info())

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 10 entries, 730 to 739
#Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
 #---  ------       --------------  -----  
 #0   年月           10 non-null     object 
 #1   國別           10 non-null     object 
 #2   台北市[金額，新台幣]  10 non-null     float64
 #3   台北市[筆數]      10 non-null     float64
#dtypes: float64(2), object(2)
#memory usage: 452.0+ bytes
#          年月   國別  台北市[金額，新台幣]    台北市[筆數]
#730  109年02月   美國  925994207.0   480931.0
#731  109年02月   日本  663748909.0   224842.0
#732  109年02月  愛爾蘭  449715911.0   437189.0
#733  109年02月   荷蘭  459261360.0  1049698.0
#734  109年02月   英國  428616667.0   114697.0
#735  109年02月  新加坡  275604137.0    77424.0
#736  109年02月   澳洲  187283530.0    25645.0
#737  109年02月   南韓   74494474.0    25638.0
#738  109年02月   法國  134882393.0    13128.0
#739  109年02月   香港  102576276.0    81481.0

import matplotlib.pyplot as plt

#處理圖表中文顯示問題
from matplotlib import rcParams
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

# 標題
plt.title('109年2月台北市市民前十大國外消費金額',fontweight = 'bold', color = 'blue')

# x 軸
plt.xlabel('國家',fontweight = 'bold') #定義X軸, 粗體
country_list = (df_tpe_10902['國別']) #取X軸值

# y 軸
plt.ylabel('消費總額(NTD)',fontweight = 'bold') #定義X軸, 粗體
amount_NTD = (df_tpe_10902['台北市[金額，新台幣]']) #取y軸值

for x,y in enumerate(amount_NTD): 
    plt.text(x,y+100,'%s' %y,ha='center') #柱體加上y軸值

plt.bar(country_list, amount_NTD)
plt.show()
plt.savefig('plot.png')