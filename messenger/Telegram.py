import telegram
import time

class Telegram:

    def __init__(self):
        # Telegram API
        self.chat_token = "5412707226:AAH0GcrnT16aKknamkQW7j0ntXi76l9cREY"
        self.chat = telegram.Bot(token = self.chat_token)
        # updates = chat.getUpdates()
        # for u in updates:
        #     print(u.message['chat']['id'])

    def sendMessege(self, img):
        bot = telegram.Bot(self.chat_token)
        text = '등록되지 않은 사람이 인식되었습니다.'
        bot.sendMessage(chat_id = "5526673347", text=text)
        bot.send_photo(chat_id = '5526673347', photo=open(img, 'rb'))

    # 텔레그램 스레드
    def send(self, q, capture_to_telegram, telegram_to_capture):
        while True:
            capture_to_telegram.wait()
            print("telegram")
            # file = q.get()
            self.sendMessege('Unknown.jpg')
            telegram_to_capture.set()
            capture_to_telegram.clear()
            while not q.empty():
                q.get()
    # def send(self, q, send, receive):
    #     while True:
    #         if receive.is_set():
    #             file = q.get()
    #             self.sendMessege('Unknown.jpg')
    #             send.set()
    #             receive.clear()
    #             while not q.empty():
    #                 q.get()

