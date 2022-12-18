import json
import datetime
import random
import pyrebase

value = 0

registered = []
registered.append({'Jang': {'name': '장성익', 'number': '201813066'}})
registered.append({'Seol': {'name': '설재혁', 'number': '201929196'}})
registered.append({'Son': {'name': '손옥무', 'number': '202159884'}})
registered.append({'Kim': {'name': '김건우', 'number': '202163104'}})

now = datetime.datetime.now()

with open('auth_database.json') as f:
    config = json.load(f)
firebase = pyrebase.initialize_app(config)
db = firebase.database()

dateList = []
data = {}
for i in range(value, -1, -1):
    newDate = now - datetime.timedelta(days=i)
    dateList.append(newDate)
for item in dateList:
    newList = []
    for i in range(8, 21):
        for j in range(0, 50, 10):
            r = random.randint(0, 100)
            if r < 1:
                r = random.randint(0, 10)
                newDate = datetime.datetime(item.year, item.month, item.day, i, j + r, item.second)
                newList.append(newDate)
    data[item] = newList


dateList = []
for key, val in data.items():
    for item in val:
        dateList.append(item)
# db.child("club").child(year).child(month).child(day).push(data)
for date in dateList:
    year = str(date)[:4]
    month = str(date)[5:7]
    day = str(date)[8:10]

    data = {}
    r = random.randint(0,3)
    for key, val in registered[r].items():
        data['engname'] = key
        for k, v in val.items():
            data[k] = v
    data['time'] = str(date)

    print(data)
    db.child("club").child(year).child(month).child(day).push(data)
