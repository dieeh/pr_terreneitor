from machine import Pin, PWM
from time import sleep

k = PWM(Pin(14, Pin.OUT), freq=1000)
j = Pin(5, Pin.OUT)
w = PWM(Pin(12, Pin.OUT), freq=1000)
q = Pin(2, Pin.OUT)


per = 90
asd = round((65535 * per) / 100)

for z in range(4):
    j.on()
    k.duty_u16(asd)
    q.on()
    w.duty_u16(asd)
    for i in range(5):
        sleep(0.5)
    sleep(2)
