import threading


class Thread_Event:
    def __init__(self):
        self.a_event = threading.Event()
        self.b_event = threading.Event()

    # 모든 이벤트 0
    def clearAll(self):
        self.a_event.clear()
        self.b_event.clear()
    
    # 모든 이벤트 1
    def setAll(self):
        self.a_event.set()
        self.b_event.set()

    # 모든 이벤트 1인지 검사
    def is_set(self):
        return self.a_event.is_set() and self.b_event.is_set()


    # 각 이벤트 얻기
    def get_a(self):
        return self.a_event
    def get_b(self):
        return self.b_event