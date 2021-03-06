p = GPIO.PWM(channel, frequency)
p.start(dc)
p.ChangeFrequency(freq) 
p.ChangeDutyCycle(dc)
p.stop()
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
  
p = GPIO.PWM(12, 50)  # 通道为 12 频率为 50Hz
p.start(0)
try:
    while 1:
        for dc in range(5, 10, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(9, 4, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
