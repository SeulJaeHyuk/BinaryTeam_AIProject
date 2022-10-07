import os

from datetime import datetime
from db.firebase_connet import Firebase


class firebase_storage(Firebase):
    def __init__(self, path='db/auth_database.json'):
        super(). __init__(path)
        self.storage = self.firebase.storage()
        
    # unknown 이미지 저장
    def img_insert(self, date):
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        self.storage.child("club").child(year).child(month).child(day).child(date[11:19]).put('Unknown.jpg')
        
    # 이미지 저장 스레드
    def insert(self, q, send, receive):
        while True:
            if receive.is_set():
                file = q.get()
                self.img_insert(str(datetime.now()))
                send.set()
                receive.clear()
    
    # log에 따라 업데이트 내용 분류
    def update(self,q, e):
        while True:
            log = q.get()
            print('log :', log)
            for key, value in log.items():
                if key == 'insert' or key == 'update':
                    self.download(value)
                elif key == 'delete':
                    self.deletefile(value)

            if q.empty():
                e.set()
                
    # 이미지 저장
    def download(self, number, path='registered/'):
        print("downloading...")
        cloud_path = 'registered/' + str(number)
        local_path = path + str(number) +'.jpg'
        self.storage.child(cloud_path).download("", local_path)
        print("download end")
        
    # 이미지 삭제
    def deletefile(self, number, path='registered/'):
        path = path + str(number) +'.jpg'
        try:
            os.remove(path)
        except:
            print(f'FileNotFoundError : {path}')
if __name__ =='__main__':
    storage = firebase_storage(path='../db/auth.json')
    storage.download(number=3, path='../registered/')
