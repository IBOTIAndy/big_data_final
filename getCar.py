import requests #抓取網頁的套件
import pandas as pd #分析資料的套件
import urllib.request #匯入套件
import zipfile
import csv
import xlrd

#https://data.ntpc.gov.tw/api/datasets/0EE4E6BF-CEE6-4EC8-8FE1-71F544015127/csv/zip

#公開的資料檔案位置
url ='https://data.ntpc.gov.tw/api/datasets/0EE4E6BF-CEE6-4EC8-8FE1-71F544015127/csv/zip'
zipName = 'zipData.zip' #壓縮檔案名稱
#下載壓縮檔並解壓縮
urllib.request.urlretrieve(url, zipName) #從url下載檔案, 並將其命名為[zipName]
zipF=zipfile.ZipFile(zipName) #開啟[zipName]壓縮檔
#file_dir = './FF'
file_dir = './' #要解壓縮的路徑 (./ = 當前目錄)
for fileName in zipF.namelist(): #壓縮檔案列表檔名
    zipF.extract(fileName, file_dir) #擷取壓縮檔案
    print(fileName) #印出解壓縮檔案名稱
zipF.close() #關檔
#壓縮檔處理完成

#開檔處理
cars = pd.read_csv(fileName, dtype = object)
print(cars)
cars = cars[['Id', 'realSequence']]
print(cars, type(cars))
cars.columns = ['routeId', 'realSequence']
print(cars, type(cars))
cars.to_csv('route_realSequence.csv')

