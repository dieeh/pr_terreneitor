from machine import Pin, PWM
from time import sleep
from motor import DCMotor

Motor1 = DCMotor(22, 33, 25)  ## Arrangement of motors
Motor2 = DCMotor(23, 26, 27)  ## --front--
Motor3 = DCMotor(13, 19, 18)  ## M2 - M1
Motor4 = DCMotor(4, 5, 17)    ## M3 - M4



Motor2.forward()
for i in range(10):
    print(i)
    Motor2.accelerate(75)
    sleep(0.5)