from machine import Pin, freq
from time import sleep, ticks_ms, ticks_diff
from motor import DCMotor, ServoMotor
from register import ShiftRegister

freq(160000000) # Boost CPU frequency to 160MHz -> Better performance

### pin assignments


# ESP8266 IO PINS
# D0 -> GPIO16  -> Sensor -> INPUT
# D1 -> GPIO5   -> Sensor -> INPUT
# D2 -> GPIO4   -> Sensor -> INPUT
# D3 -> GPIO0   -> Sensor -> INPUT
# D4 -> GPIO2   -> Sensor -> INPUT
# D5 -> GPIO14  -> Register -> OUTPUT
# D6 -> GPIO12  -> Register -> OUTPUT
# D7 -> GPIO13  -> Register -> OUTPUT
# D8 -> GPIO15  -> ServoMotor -> PWM OUTPUT

# SN74HC595 REGISTER OUTPUT PINS
# Qa -> I0 -> DCMotor1_Forward
# Qb -> I1 -> DCMotor1_Backward
# Qc -> I2 -> DCMotor2_Forward
# Qd -> I3 -> DCMotor2_Backward
# Qe -> I4 -> DCMotor3_Forward
# Qf -> I5 -> DCMotor3_Backward
# Qg -> I6 -> DCMotor4_Forward
# Qh -> I7 -> DCMotor4_Backward

MotorPins = ShiftRegister(14, 12, 13)

#Init Register
MotorPins.setOutputs([0,0,0,0,0,0,0,0])
MotorPins.latch()

Motor1 = DCMotor(MotorPins, 0, 1)  ## Arrangement of motors
Motor2 = DCMotor(MotorPins, 2, 3)  ## --front--
Motor3 = DCMotor(MotorPins, 4, 5)  ## M1 - M2
Motor4 = DCMotor(MotorPins, 6, 7)  ## M3 - M4
Servo = ServoMotor(15)


def turn_right(inv=False):
    if inv:
        Servo.movement(45)
        sleep(0.2)
        Servo.movement(45)
    else:
        Servo.movement(135)
        sleep(0.2)
        Servo.movement(135)


def turn_left(inv=False):
    if inv:
        Servo.movement(135)
        sleep(0.2)
        Servo.movement(135)
    else:
        Servo.movement(45)
        sleep(0.2)
        Servo.movement(45)


def center():
    Servo.movement(90)
    sleep(0.2)
    Servo.movement(90)


SensorIn_1 = Pin(16, Pin.IN)
SensorIn_2 = Pin(5, Pin.IN)  ## Arrangement of sensors
SensorIn_3 = Pin(4, Pin.IN)  ## -- front --
SensorIn_4 = Pin(0, Pin.IN)  ## 1,2,3,4,5
SensorIn_5 = Pin(2, Pin.IN)  ## values: 0 for black, 1 for white

# region  
## Sersor info
# (SensorIn_1 == 1) and (SensorIn_2 == 1) and (SensorIn_3 == 0) and (SensorIn_4 == 1) and (SensorIn_5 == 1)

# [0,0,0,0,0] (SensorIn_1 == 0) and (SensorIn_2 == 0) and (SensorIn_3 == 0) and (SensorIn_4 == 0) and (SensorIn_5 == 0) quiet
# [0,0,0,0,1] (SensorIn_1 == 0) and (SensorIn_2 == 0) and (SensorIn_3 == 0) and (SensorIn_4 == 0) and (SensorIn_5 == 1) quiet
# [0,0,0,1,0] (SensorIn_1 == 0) and (SensorIn_2 == 0) and (SensorIn_3 == 0) and (SensorIn_4 == 1) and (SensorIn_5 == 0) left
# [0,0,0,1,1] (SensorIn_1 == 0) and (SensorIn_2 == 0) and (SensorIn_3 == 0) and (SensorIn_4 == 1) and (SensorIn_5 == 1) left
# [0,0,1,0,0] (SensorIn_1 == 0) and (SensorIn_2 == 0) and (SensorIn_3 == 1) and (SensorIn_4 == 0) and (SensorIn_5 == 0) quiet
# [0,0,1,0,1] (SensorIn_1 == 0) and (SensorIn_2 == 0) and (SensorIn_3 == 1) and (SensorIn_4 == 0) and (SensorIn_5 == 1) quiet
# [0,0,1,1,0] (SensorIn_1 == 0) and (SensorIn_2 == 0) and (SensorIn_3 == 1) and (SensorIn_4 == 1) and (SensorIn_5 == 0) left
# [0,0,1,1,1] (SensorIn_1 == 0) and (SensorIn_2 == 0) and (SensorIn_3 == 1) and (SensorIn_4 == 1) and (SensorIn_5 == 1) left
# [0,1,0,0,0] (SensorIn_1 == 0) and (SensorIn_2 == 1) and (SensorIn_3 == 0) and (SensorIn_4 == 0) and (SensorIn_5 == 0) right
# [0,1,0,0,1] (SensorIn_1 == 0) and (SensorIn_2 == 1) and (SensorIn_3 == 0) and (SensorIn_4 == 0) and (SensorIn_5 == 1) right
# [0,1,0,1,0] (SensorIn_1 == 0) and (SensorIn_2 == 1) and (SensorIn_3 == 0) and (SensorIn_4 == 1) and (SensorIn_5 == 0) forward
# [0,1,0,1,1] (SensorIn_1 == 0) and (SensorIn_2 == 1) and (SensorIn_3 == 0) and (SensorIn_4 == 1) and (SensorIn_5 == 1) forward
# [0,1,1,0,0] (SensorIn_1 == 0) and (SensorIn_2 == 1) and (SensorIn_3 == 1) and (SensorIn_4 == 0) and (SensorIn_5 == 0) right
# [0,1,1,0,1] (SensorIn_1 == 0) and (SensorIn_2 == 1) and (SensorIn_3 == 1) and (SensorIn_4 == 0) and (SensorIn_5 == 1) right
# [0,1,1,1,0] (SensorIn_1 == 0) and (SensorIn_2 == 1) and (SensorIn_3 == 1) and (SensorIn_4 == 1) and (SensorIn_5 == 0) forward
# [0,1,1,1,1] (SensorIn_1 == 0) and (SensorIn_2 == 1) and (SensorIn_3 == 1) and (SensorIn_4 == 1) and (SensorIn_5 == 1) left
# [1,0,0,0,0] (SensorIn_1 == 1) and (SensorIn_2 == 0) and (SensorIn_3 == 0) and (SensorIn_4 == 0) and (SensorIn_5 == 0) forward
# [1,0,0,0,1] (SensorIn_1 == 1) and (SensorIn_2 == 0) and (SensorIn_3 == 0) and (SensorIn_4 == 0) and (SensorIn_5 == 1) forward
# [1,0,0,1,0] (SensorIn_1 == 1) and (SensorIn_2 == 0) and (SensorIn_3 == 0) and (SensorIn_4 == 1) and (SensorIn_5 == 0) left
# [1,0,0,1,1] (SensorIn_1 == 1) and (SensorIn_2 == 0) and (SensorIn_3 == 0) and (SensorIn_4 == 1) and (SensorIn_5 == 1) left
# [1,0,1,0,0] (SensorIn_1 == 1) and (SensorIn_2 == 0) and (SensorIn_3 == 1) and (SensorIn_4 == 0) and (SensorIn_5 == 0) forward
# [1,0,1,0,1] (SensorIn_1 == 1) and (SensorIn_2 == 0) and (SensorIn_3 == 1) and (SensorIn_4 == 0) and (SensorIn_5 == 1) forward
# [1,0,1,1,0] (SensorIn_1 == 1) and (SensorIn_2 == 0) and (SensorIn_3 == 1) and (SensorIn_4 == 1) and (SensorIn_5 == 0) left
# [1,0,1,1,1] (SensorIn_1 == 1) and (SensorIn_2 == 0) and (SensorIn_3 == 1) and (SensorIn_4 == 1) and (SensorIn_5 == 1) left
# [1,1,0,0,0] (SensorIn_1 == 1) and (SensorIn_2 == 1) and (SensorIn_3 == 0) and (SensorIn_4 == 0) and (SensorIn_5 == 0) right
# [1,1,0,0,1] (SensorIn_1 == 1) and (SensorIn_2 == 1) and (SensorIn_3 == 0) and (SensorIn_4 == 0) and (SensorIn_5 == 1) right
# [1,1,0,1,0] (SensorIn_1 == 1) and (SensorIn_2 == 1) and (SensorIn_3 == 0) and (SensorIn_4 == 1) and (SensorIn_5 == 0) forward
# [1,1,0,1,1] (SensorIn_1 == 1) and (SensorIn_2 == 1) and (SensorIn_3 == 0) and (SensorIn_4 == 1) and (SensorIn_5 == 1) forward
# [1,1,1,0,0] (SensorIn_1 == 1) and (SensorIn_2 == 1) and (SensorIn_3 == 1) and (SensorIn_4 == 0) and (SensorIn_5 == 0) right
# [1,1,1,0,1] (SensorIn_1 == 1) and (SensorIn_2 == 1) and (SensorIn_3 == 1) and (SensorIn_4 == 0) and (SensorIn_5 == 1) right
# [1,1,1,1,0] (SensorIn_1 == 1) and (SensorIn_2 == 1) and (SensorIn_3 == 1) and (SensorIn_4 == 1) and (SensorIn_5 == 0) right
# [1,1,1,1,1] (SensorIn_1 == 1) and (SensorIn_2 == 1) and (SensorIn_3 == 1) and (SensorIn_4 == 1) and (SensorIn_5 == 1) quiet
#endregion

#region
# [0,1,0,1,0] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) forward
# [0,1,0,1,1] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) forward
# [0,1,1,1,0] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) forward
# [1,0,0,0,0] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) forward
# [1,0,0,0,1] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) forward
# [1,0,1,0,0] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) forward
# [1,0,1,0,1] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) forward
# [1,1,0,1,0] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) forward
# [1,1,0,1,1] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) forward
# [0,1,0,0,0] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) right
# [0,1,0,0,1] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) right
# [0,1,1,0,0] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) right
# [0,1,1,0,1] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) right
# [1,1,0,0,0] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) right
# [1,1,0,0,1] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) right
# [1,1,1,0,0] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) right
# [1,1,1,0,1] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) right
# [1,1,1,1,0] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) right
# [0,0,0,1,0] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) left
# [0,0,0,1,1] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) left
# [0,0,1,1,0] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) left
# [0,0,1,1,1] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) left
# [0,1,1,1,1] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) left
# [1,0,0,1,0] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) left
# [1,0,0,1,1] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) left
# [1,0,1,1,0] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) left
# [1,0,1,1,1] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) left
# [0,0,0,0,0] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) backwards
# [0,0,0,0,1] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) backwards
# [0,0,1,0,0] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) backwards
# [0,0,1,0,1] ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) backwards
# [1,1,1,1,1] ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) backwards
#endregion

flag = True
while flag:
    while (
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1))
    ):
        print('1')

    while (
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0))
    ):
        print('2'):

    while (
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1))
    ):
        print('3')

    while (
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1))
    ):
        print('4')

    startTime = ticks_ms()
    while(((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1))):
        if (ticks_diff(ticks_ms(), startTime)/1000 > 5):    
            print("Longer than 5 seconds")
            flag = False
            break


#Exit protocol
freq(80000000)
MotorPins.setOutputs([0,0,0,0,0,0,0,0])
MotorPins.latch()