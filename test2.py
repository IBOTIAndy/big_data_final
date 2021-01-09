import urllib.request #匯入套件
import zipfile
import csv
import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np
import seaborn as sns
from pylab import mpl

mpl.rcParams['axes.unicode_minus'] = False

pd.set_option("display.max_rows", 200)    #設定最大能顯示1000rows
pd.set_option("display.max_columns", 200) #設定最大能顯示1000columns
i=0

df=pd.read_csv('end_marge.csv')

df = df[df["station_n"] != 0]
#df = df[df["711_n"] >= 3]
df = df[df["711_n"] < 30]
print(df)
x = np.linspace(0, 400, 40)
y = np.linspace(0, 25000, 40)
plt.scatter(x=df['station_n'], y=df['total_sequence'])
plt.xlabel("station_n")
plt.ylabel("total_sequence") #total_sequence or station_n
plt.plot(x, y, c="y")
plt.title('station & sequence')
#image=df.plot.scatter(x='station_n', y='total_sequence',title='total_sequence'
plt.savefig("figure.png")
#fig = image.get_figure()                      #取得圖片
#fig.savefig('figure.png')                     #保存成png
