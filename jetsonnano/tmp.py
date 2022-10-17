import time
import Jetson.GPIO as GPIO
output_pin = 18  # BCM pin 18, BOARD pin 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
try:
    time.sleep(2)
    GPIO.output(output_pin, GPIO.LOW)
finally:
    GPIO.cleanup()