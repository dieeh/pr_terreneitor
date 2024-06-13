from machine import Pin, PWM
from time import sleep
from motores import DCMotor

p1 = Pin(5, Pin.OUT)  # D1
d1 = Pin(4, Pin.OUT)  # D2
d1_1 = Pin(0, Pin.OUT)  # D3

motor1_L = DCMotor(p1, d1, d1_1, 500, 80)

flag = True
motor1_L.accelerate()
while flag:
    sleep(5)
    flag = False
motor1_L.stop()
