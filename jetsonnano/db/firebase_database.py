import random
import threading
import time
from queue import Queue
import datetime
import pyrebase
import json

from db.firebase_connet import Firebase

class firebase_database(Firebase):

    def __init__(self, delay = 10, path='db/auth_database.json'):
        super().__init__(path)
        self.registered_data = {}
        self.delay = delay
        self.last_person = {}
        self.db= self.firebase.database()

    def insert(self, q):
        while True:
            name = q.get()
            self.set(name)

    # firebase에 추가
    def set(self, name):
        now = datetime.datetime.now()
        date = str(now)
        data = {}

        # 깊은 복사
        data['engname'] = name
        data['number'] = self.registered_data[name]['number']
        data['name'] = self.registered_data[name]['name']
        data['time'] = date

        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        if self.cooldowncheck(name):
        # if True:
            self.last_person['number'] = data['number']
            self.last_person['engname'] = name
            self.last_person['name'] = data['name']
            self.last_person['time'] = now
            self.db.child("club").child(year).child(month).child(day).push(data)
            return True
        else:
            return False

    # 딜레이 계산
    def cooldowncheck(self, name): # 마지막과 동일하면 False DB저장하려면 True
        if self.last_person == {}:
            print('true')
            return True
        else:
            # 이름이 다를시 바로 저장
            if name != self.last_person['engname']:
                return True

            now = datetime.datetime.now()
            date = self.last_person['time']
            difference = (now - date).seconds
            if difference > self.delay:
                return True
            else:
                return False
        print("error")

    # 이름 변경 (학번->영어이름)
    def changeName(self, numbers):
        while True:
            self.registered_data = {}
            names = []
            # numbers = list(self.db.child("registered").shallow().get().val())
            for number in numbers:
                name = self.db.child('registered').child(number).child('name').get().val()
                engname = self.db.child('registered').child(number).child('engname').get().val()
                self.registered_data[engname] = {
                    'number': number,
                    'name' : name
                }
                names.append(engname)
            return names

    # realdatabase 감시 스레드
    def observer(self, q, e):
        # data = {'insert': '201813066'}
        # self.db.child("log").push(data)
        while True:
            registered = self.db.child("log").get()
            if registered != None and registered.val() != None:
                e.set()
                for people in registered.each():
                    key = people.key()
                    data = self.db.child('log').child(key).get().val()
                    data = dict(data)
                    q.put(data)
                    self.db.child('log').child(key).remove()

if __name__ == '__main__':

    # def randData(startDate):
    #     start = datetime.datetime(startDate)
    # db = firebase_database(path='./auth_database.json')

    # 학생 정보 임의 추가
    # db.registered_data ={'Jang': {'number': '201813066', 'name': '장성익'}, 'Seol': {'number': '201929196', 'name': '설재혁'}, 'Son': {'number': '202159884', 'name': '손옥무'}, 'Kim': {'number': '202163104', 'name': '김건우'}}
    # db.set('Jang')

    # 랜덤 추가

    registered_data = {'Jang': {'number': '201813066', 'name': '장성익'}, 'Seol': {'number': '201929196', 'name': '설재혁'}, 'Son': {'number': '202159884', 'name': '손옥무'}, 'Kim': {'number': '202163104', 'name': '김건우'}}


    now = datetime.datetime.now()

    with open('auth_database.json') as f:
        config = json.load(f)
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    dateList = []
    data = {}
    for i in range(10):
        newDate = now - datetime.timedelta(days=i)
        dateList.append(newDate)
    for item in dateList:
        newList = []
        for i in range(8, 21):
            for j in range(0, 50, 10):
                r = random.randint(0,100)
                if r<10:
                    r = random.randint(0,10)
                    newDate = datetime.datetime(item.year, item.month, item.day, i, j+r, item.second)
                    newList.append(newDate)
        data[item] = newList

    for key, val in data.items():
        for item in val:
            print(key," a " ,item)
    # db.child("club").child(year).child(month).child(day).push(data)