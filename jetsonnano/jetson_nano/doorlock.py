import Jetson.GPIO as GPIO
import time

class Doorlock:
    def __init__(self) -> None:
        # Pin Definitions
        self.output_pin = 18  # BCM pin 18, BOARD pin 12

    # 도어락 열기
    def open(self):
        # time.sleep(3)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.output_pin, GPIO.OUT, initial=GPIO.HIGH)

        print("Door Open")
    
        try:
            for i in range(1, 3):
                time.sleep(1)
                GPIO.output(self.output_pin, GPIO.LOW)
                
        finally:
            GPIO.cleanup()
            pass
        time.sleep(10)

    # 도어락 여는 스레드
    def action(self, q):
        while True:
            name = q.get()
            self.open()
            while not q.empty():
                q.get()
if __name__ == "__main__":
    d = Doorlock()
    d.open()