from machine import Pin, PWM
from time import sleep
from motor import DCMotor

Motor1 = DCMotor(22, 33, 25, 2000)  ## Arrangement of motors
Motor2 = DCMotor(23, 26, 27, 2000)  ## --front--
Motor3 = DCMotor(13, 19, 18, 2000)  ## M2 - M1
Motor4 = DCMotor(4, 16, 17, 2000)    ## M3 - M4


Motor3.forward()
Motor4.forward()

for i in range(6, 11):
    print(i*10)
    for j in range(35):
        Motor3.accelerate(i*10)
        Motor4.accelerate(i*10)
        sleep(0.2)