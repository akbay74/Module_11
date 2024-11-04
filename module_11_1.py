import requests
from datetime import datetime
import pandas
from pprint import pprint
import matplotlib.pyplot as plt

# Формируем запрос стоимости акций с помощью библиотеки requests
stock = ['GAZP', 'SBER', 'MOEX', 'ROSN', 'GMKN']
candles = 'D'
date_to_unix_start = int(datetime(2024, 10, 1).timestamp())
date_to_unix_end = int(datetime(2024, 10, 30).timestamp())
URL_BGN = 'https://api.bcs.ru/udfdatafeed/v1/history?symbol='
URL_END = f'&resolution={candles}&from={date_to_unix_start}&to={date_to_unix_end}'
vol_stock = {}
for st in stock:
    URL = URL_BGN + st + URL_END
    req = requests.get(URL)
    req = req.json()
    date = [datetime.fromtimestamp(dt).strftime('%d-%m') for dt in req['t']]
    vol_stock[st] = (req['c'], date)
    print(st, vol_stock[st])


# Формируем список стоимости акций для записи в файл
column_list = ['Ticker']
column_list =column_list + [vol_stock[stock[0]][1][i] for i in range(len(vol_stock[stock[0]][1]))]
val_list = []
for st in vol_stock.keys():
    line = [st] + [vol_stock[st][0][i] for i in range(len(vol_stock[st][0]))]
    val_list.append(line)

# Сохраняем полученные данные в файл .xlsx, используя pandas
df1 = pandas.DataFrame(val_list, columns=column_list)
with pandas.ExcelWriter('volume_stock.xlsx') as file:
    df1.to_excel(file)

# Построение графиков на основе данных из файла .xlsx, с помощью matplotlib
stock_data = pandas.read_excel('volume_stock.xlsx')
pprint(stock_data)
plt.xlabel('Дата')
plt.ylabel('Цена акций')
x = column_list[1:]
for i in range(len(stock_data)):
    y = stock_data.values[i][2:]
    plt.plot(x, y, marker='o', markersize=5, label=stock_data.values[i][1])
    plt.legend()
plt.show()
