# import datetime
# import json
# import pyrebase
#
# path = 'db/auth_database.json'
# with open(path) as f:
#     config = json.load(f)
# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
#
# name = 'Jang'
#
# registered_data = {'Jang': {'number': '201813066', 'name': '장성익'}, 'Seol': {'number': '201929196', 'name': '설재혁'}, 'Son': {'number': '202159884', 'name': '손옥무'}, 'Kim': {'number': '202163104', 'name': '김건우'}}
#
# now = datetime.datetime.now()
# date = str(now)
# print('date :',type(date))
# data = registered_data[name]
# data['time'] = date
# print('time :',type(data['time']))
# data['engname'] = name
# year = date[:4]
# month = date[5:7]
# day = date[8:10]
# last_person = data
# print('data :',data)
# last_person['time'] = now
# print('p :', id(last_person['time']))
# print('date :',id(data['time']))
#
# db.child("club").child(year).child(month).child(day).push(data)





# for i in range(123):
#     print(f"INSERT INTO board(subject, content, writer, regdate) VALUES('안녕{i}', '반가워요{i}', 'gildong{i}', SYSDATE());")

# for i in range(500):
#     print(f"insert into member values('id{i}', '{i}','이름{i}','{i}@gmail.com', now());");

from collections import deque

dq=deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
print(dq)
print(dq.pop())
print(dq.pop())
print(dq.pop())
print(dq)