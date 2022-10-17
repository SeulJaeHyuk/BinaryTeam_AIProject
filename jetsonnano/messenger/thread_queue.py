import time
from queue import Queue


class Thread_Queue:
    def __init__(self, delay=5):
        self.realtime_queue = Queue()
        self.update_queue = Queue()
        self.storage_queue = Queue()
        self.telegram_queue = Queue()
        self.doorlock_queue = Queue()
        self.capture_queue = Queue()
        self.delay = delay
        self.known = time.time()
        self.unKnown = time.time()

    def get_realtime(self):
        return self.realtime_queue
    def get_update(self):
        return self.update_queue
    def get_storage(self):
        return self.storage_queue
    def get_telegram(self):
        return self.telegram_queue
    def get_doorlock(self):
        return self.doorlock_queue
    def get_capture(self):
        return self.capture_queue

    def put(self, keyword):
        if time.time() - self.known > self.delay:
            self.realtime_queue.put(keyword)
            self.doorlock_queue.put(keyword)

    def put_img(self, name, frame):
        # if time.time() - self.unKnown > self.delay:
        if self.capture_queue.empty():
            data = { name : frame}
            self.capture_queue.put(data)
            # self.telegram_queue.put(name)
            # self.storage_queue.put(name)
