import pandas as pd #分析資料的套件
import csv

file_711 = "sorted_7_11.csv"
file_bus = "bus_2.csv"
f711 = pd.read_csv(file_711, dtype = object)
fbus = pd.read_csv(file_bus, dtype = object)
#print("f711:\n", f711)
#print("fbus:\n", fbus)
fbus.columns=["id", "address", "realSequence"]
#print("fbus:\n", fbus)

#留下新北市, 其他去掉
selectCity = "新北市"
f711 = f711[f711["city"] == selectCity]
f711 = f711.reset_index(drop=True)
#print(f711)

#[城市, 地址, 7-11數量, 站牌數量, 總班次]
#marge = pd.DataFrame(columns=["city", "address", "711_n", "station_n", "total_sequence"])
marge = []
#print(marge)

i=0
for store in f711.iterrows():
    #print("i=%d\n" %i, store)
    station_n = 0
    total_sequence = 0
    for bus in fbus.iterrows():
        #print("bus: ", bus[1]["address"])
        if(store[1]["road_ja"] == bus[1]["address"]): #找到路段上的站牌
            city = store[1]["city"]
            address = store[1]["road_ja"]
            s7_11n = store[1]["n"]
            station_n = station_n + 1 #站牌數量 +1
            total_sequence = total_sequence + int(bus[1]["realSequence"]) #班次相加
    newList = {"city": city, "address": address, "711_n": s7_11n, "station_n": station_n, "total_sequence": total_sequence}
    #newList = [city, address, s7_11n, station_n, total_sequence]
    print("%d) " %i, newList)
    marge.append(newList)
    #print(marge)
    i = i + 1
#    if i == 10:
#        break
marge = pd.DataFrame(marge)

print(marge)
marge.to_csv('end_marge.csv', encoding="UTF-8", index=False)


