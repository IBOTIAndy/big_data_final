#抓取7-eleven各門市資訊
import requests #抓取網頁的套件
import pandas as pd #分析資料的套件
# 建立一個縣市的list
city = ['新北市']
#city = ['基隆市', '台北市', '新北市', '桃園市', '新竹市','新竹縣','苗栗縣','台中市','彰化縣', '雲林縣', '南投縣', '嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣', '連江縣', '金門縣', '澎湖縣']

#使用迴圈依序取得每一個城市的門市資訊， enumerate(city) 產生[0, 基隆市] [1, 台北市][2, 新北市][3, 桃園市]
for index, city in enumerate(city):
    #剛在網頁開發者模式觀察到的Post發出的資訊是那些
    data = {'strTargetField':'COUNTY','strKeyWords':'%s' % city}
    #res 取得網頁所有資料
    res = requests.post('http://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    # 第一次迴圈
    if index == 0:
        #網頁資料的形式是table，使用panda的 read_html 取得資料 [0]第一欄資料
        # res.txt 網頁資料中的文字，[0]第一欄資料, header=0 不要第一列標頭資料
        df_7_11_store = pd.read_html(res.text, header=0)[0]
        #建立dataframe，將城市填入。
        df_7_11_store['縣市'] = city
    # 第二次迴圈以上就將資訊直接append到dataframe裡
    if index > 0:
        oneCity_store = pd.read_html(res.text, header=0)[0]
        oneCity_store['縣市'] = city
        df_7_11_store = df_7_11_store.append(oneCity_store)
        #print(oneCity_store)
    #印出查詢資料進度, shape[0] 查詢本次城市取得資料的筆數
    # (1)
    #print('%2d) %-*s 門市數量: %4d' % (index+1, 5, city, pd.read_html(res.text, header=0)[0].shape[0]))
#將資料輸出成Excel
df_7_11_store.to_excel('7_11.xlsx', encoding="UTF-8", index=False)


#已將各縣市的7-11放入execl
dicfile = pd.read_excel('7_11.xlsx') #開啟已經儲存的execl
realrow, realcol = dicfile.shape
k=0
table = []
table2 = []
for fullAddress in dicfile['地址']: 
#    if k >= 10:
#        break
#    k=k+1
    #縣市
#    print(fullAddress)
    start = fullAddress.find('縣') + 1
    if start == 0:
        start = fullAddress.find('市') + 1    
    end = len(fullAddress)
    address = fullAddress[start:len(fullAddress)]
#    print("1. 去除\"縣, 市\": %s\nstart: %d, end=len(fullAddress)" %(address, start))

    #區市鄉
    start = address.find('區') + 1
    if start == 0:
        start = address.find('市') + 1    
    if start == 0:
        start = address.find('鄉') + 1    
    if start == 0:
        start = address.find('鎮') + 1    
    end = len(address)
    roun = address[0:start]
    address = address[start:len(address)]
#    print("2. 去除\"區, 市, 鄉, 鎮\": %s\nstart: %d, end=len(address)" %(address, start))
   
    #里, 村
    start = address.find('里') + 1
    if start == 0:
        start = address.find('村') + 1    
    end = len(address)
    address = address[start:len(address)]
#    print("3. 去除\"里, 村\": %s\nstart: %d, end=len(address)" %(address, start))
    
    start = address.find('鄰') + 1    
    if start == 0:
        start = address.find('或') + 1
    end = len(address)
    address = address[start:len(address)]
#    print("4. 去除\"鄰, 或\": %s\nstart: %d, end=len(address)" %(address, start))

    #路
    road = ""
    end1 = address.find('路')
    if end1 != -1:
        road = address[0:end1 + 1]
    #街
    ja = ""
    end2 = address.find('街')
    if end2 != -1:
        ja = address[0:end2 + 1]

#    print("road:", road)      #輸出檢查
#    print("ja:", ja)      #輸出檢查
    
    #取得所在縣市
    tail = len(fullAddress)
    end = fullAddress.find('縣') + 1
    if end == 0:
        end = fullAddress.find('市') + 1
    cityname = fullAddress[0:end]
#    print("取得所在城市: %s" %cityname)
#    print("\n\n")
    start = -1
    if ((len(road) - len("捷運地下街")) > 0):
        if road != "":
            #print("test (%s, %s)" %(road, ja))
            if start == -1:
                start = road.rfind(".")
            if start == -1:
                start = road.rfind("、")
            if start == -1:
                start = road.rfind("(")
            if start == -1:
                start = road.rfind("區")
            if start == -1:
                start = road.rfind("號")
            #print("start: %d" %start)
            if start != -1:
                road = road[start+1:len(road)]
    if((len(ja) - len("捷運地下街")) > 0):
        if ja != "":
            #print("test (%s, %s)" %(road, ja))
            if start == -1:
                start = ja.rfind(".")
            if start == -1:
                start = ja.rfind("、")
            if start == -1:
                start = ja.rfind("(")
            if start == -1:
                start = ja.rfind("區")
            if start == -1:
                start = ja.rfind("號")
            if start != -1:
                ja = ja[start+1:len(ja)]
#裁剪完畢

    #路
    if road != "":
        flag = True
        for i in table:
            if cityname == i["city"] and road == i["road_ja"]:
                flag = False
                i['n'] = i['n'] + 1
                break
        if flag:
            newRoad = {"city":cityname, "road_ja": road, "n": 1}
            table.append(newRoad.copy())
        #print("%s, %s, %s" %(cityname, roun, road))
    #街
    if ja != "":
        flag = True
        for i in table:
            if cityname == i["city"] and ja == i["road_ja"]:
                flag = False
                i['n'] = i['n'] + 1
                break
        if flag:
            newJa = {"city":cityname, "road_ja": ja, "n": 1}
            table.append(newJa.copy())
        #print("%s, %s, %s" %(cityname, roun, ja))
pd_table = pd.DataFrame(columns=["city", "road_ja", "n"], data=table)
pd_table = pd_table.sort_values(by='n', ascending=False) #降序
pd_table = pd_table.reset_index(drop=True) #整理index
print(pd_table)
pd_table.to_csv('sorted_7_11.csv', encoding="UTF-8", index=False)
cutrow, cutcol = pd_table.shape
print(realrow, cutrow)
print("成功率：%.2f％" %((cutrow/realrow)*100))
