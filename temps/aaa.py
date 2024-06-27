from machine import Pin, PWM
from time import sleep


vel1 = PWM(Pin(5, Pin.OUT), freq=500)  # D1
vel2 = PWM(Pin(13, Pin.OUT), freq=500)  # D7

dir1 = Pin(4, Pin.OUT)  # D2
dir1_1 = Pin(0, Pin.OUT)  # D3
dir1_1.off()
dir2 = Pin(14, Pin.OUT)  # D5
dir2_1 = Pin(12, Pin.OUT)  # D6
dir2_1.off()

per = 100
k = round((1023 * per) / 100)

for i in range(3):
    dir1.on()
    vel1.duty(k)
    dir2.on()
    vel2.duty(k)
    sleep(0.2)
    for j in range(10):
        sleep(0.2)
        print(j)
    vel1.duty(0)
    vel2.duty(0)
    sleep(1)
    dir1.off()
    dir2.off()
