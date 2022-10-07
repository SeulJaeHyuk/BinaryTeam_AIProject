from queue import Queue


class Thread_Queue:
    def __init__(self):
        self.realtime_queue = Queue()
        self.update_queue = Queue()
        self.storage_queue = Queue()
        self.telegram_queue = Queue()
        self.doorlock_queue = Queue()
        self.capture_queue = Queue()

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
        self.realtime_queue.put(keyword)
        if self.doorlock_queue.empty():
            self.doorlock_queue.put(keyword)

    def put_img(self, name, frame):
        data = { name : frame}
        self.capture_queue.put(data)
        self.storage_queue.put(name)
        self.telegram_queue.put(name)
