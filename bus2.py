import urllib.request #匯入套件
import zipfile
import csv
import pandas as pd
def main():
    test1()
    test2()

def test1():
    # 公開資料檔案
    name = ['id','地址']
    url ='https://data.ntpc.gov.tw/api/datasets/34B402A8-53D9-483D-9406-24A682C2D6DC/csv/zip'
    zipName = 'F.zip' #壓縮檔案名稱
    urllib.request.urlretrieve(url,zipName) #下載壓縮檔
    f=zipfile.ZipFile(zipName) #開啟壓縮檔
    #file_dir = './FF'
    file_dir = './' #解壓縮目錄
    for fileName in f.namelist(): #壓縮檔案列表檔名
        f.extract(fileName,file_dir) #擷取壓縮檔案
        print(fileName) #印出解壓縮檔案名稱
    f.close() #關檔
    f = open(fileName,'r',encoding = 'utf8') #開啟CSV檔案，，唯讀 utf-8解碼
    plots = csv.reader(f, delimiter=',') #取取CSV檔案

    arr1 = [] #包id、路或街名
    arr2 = [] #包arr1成為二微陣列
    arr3 = [] #把arr2相同的去掉再丟進來
    bug1 = [] #引導arr2找出自身的相同資料
    i=0
    f = open(fileName,'r',encoding = 'utf8') #開啟CSV檔案，，唯讀 utf-8解碼
    plots = csv.reader(f, delimiter=',') #取取CSV檔案

    out = 0
    Address = []
    for row in plots: 
        #縣市
    #    print(Address)
        out2 = 0
        Address = row[9]
        #print(Address)
        if '新北市' in Address or '台北縣' in Address:
            out = 1    #判斷如果有新北市或台北縣等於1
            out2 = 1    #二次確認，防止find找到'市'但是不是包含在新北市或台北縣
        start = Address.find('縣') + 1
        if start == 0:
            start = Address.find('市') + 1
        if start > 1 and out2 == 0:
            out = 0
        end = len(Address)
        address = Address[start:len(Address)]

        #區市鄉
        start = address.find('區') + 1
        if start == 0:
            start = address.find('市') + 1  
            if start > 1 and out2 == 0:
                out = 0
        if start == 0:
            start = address.find('鄉') + 1    
        if start == 0:
            start = address.find('鎮') + 1    
        end = len(address)
        address = address[start:len(address)]
    
        #里, 村
        start = address.find('里') + 1
        if start == 0:
            start = address.find('村') + 1    
        end = len(address)
        address = address[start:len(address)]
        
        start = address.find('鄰') + 1    
        if start == 0:
            start = address.find('或') + 1
        end = len(address)
        address = address[start:len(address)]
        #路
        road = ""
        end1 = address.find('路') + 1
        road = address[0:end1]
        #街
        ja = ""
        end2 = address.find('街') + 1
        ja = address[0:end2]
        
        #取得所在縣市
        tail = len(Address)
        end = Address.find('縣') + 1
        if end == 0:
            end = Address.find('市') + 1
        cityname = Address[0:end]

        start = -1
        #路
        if road != "" and out == 1:
            if ((len(road) - len("捷運地下街")) > 0):
                if start == -1:
                    start = road.rfind("+")
                if start == -1:
                    start = road.rfind("(")
                if start == -1:
                    start = road.rfind("與")
                if start == -1:
                    start = road.rfind("區")
                if start != -1:
                    road = road[start+1:len(road)]
            arr1.append(row[1])
            arr1.append(road)
            arr2.append(arr1)
        arr1=[]   
        i+=1
        #街
        if ja != "" and out == 1:
            if((len(ja) - len("捷運地下街")) > 0):
                if start == -1:
                    start = ja.rfind("+")
                if start == -1:
                    start = ja.rfind("(")
                if start == -1:
                    start = ja.rfind("段")
                if start == -1:
                    start = ja.rfind("與")
                if start == -1:
                    start = ja.rfind("號")
                if start == -1:
                    start = ja.rfind("路")
                if start != -1:
                    ja = ja[start+1:len(ja)]
            arr1.append(row[1])
            arr1.append(ja)
            arr2.append(arr1)
        arr1=[]   
        i+=1
        
    for i in range(len(arr2)):    #去掉相同的資料
        if bug1 != arr2[i]:
            arr3.append(arr2[i])
        bug1 = arr2[i]
        
    df_bus = pd.DataFrame(columns=name,data=arr3)    #arr3存到df_bus
    df_bus.to_csv('bus_1.csv', encoding="UTF-8", index=False)  #df_bus轉成excel檔
def test2():
    arr1=[]
    arr2=[]
    arr3=[]
    arr4=[]
    name=['id','地址','總班次']
    i=0
    f1 = open('route_realSequence.csv','r',encoding = 'utf8')
    plots1 = csv.reader(f1, delimiter=',')
    f2 = open('bus_1.csv','r',encoding = 'utf8')
    plots2 = csv.reader(f2, delimiter=',')
    for row in plots2:
        arr1.append(row)
    for row2 in plots1:
        arr2.append(row2)

    for row in arr1:
        for row2 in arr2:
            i+=1
            if row[0] == row2[1]:
                arr3.append(row[0])
                arr3.append(row[1])
                arr3.append(row2[2])
                arr4.append(arr3)
            arr3=[]
    df_bus = pd.DataFrame(columns=name,data=arr4)    #arr4存到df_bus
    df_bus.to_csv('bus_2.csv', encoding="UTF-8", index=False)  #df_bus轉成csv檔


main()

