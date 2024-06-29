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

MotorPins = ShiftRegister(14, 12, 13)  ## Init Register
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


SensorIn_1 = Pin(16, Pin.IN, value=0)
SensorIn_2 = Pin(5, Pin.IN, value=0)  ## Arrangement of sensors
SensorIn_3 = Pin(4, Pin.IN, value=0)  ## -- front --
SensorIn_4 = Pin(0, Pin.IN, value=0)  ## 1,2,3,4,5
SensorIn_5 = Pin(2, Pin.IN, value=0)  ## values: 0 for black, 1 for white

debug_list = []
flag = True
while flag:
    debug_timer1 = ticks_ms()
    if (
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
        Motor1.accelerate()
        Motor2.accelerate()
        Motor3.accelerate()
        Motor4.accelerate()

    if (
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
        turn_right()
        sleep(0.2)
        Motor1.accelerate()
        Motor2.stop()
        Motor3.accelerate()
        Motor4.accelerate()
    else:
        center()

    if (
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
        turn_left()
        sleep(0.2)
        Motor1.stop()
        Motor2.accelerate()
        Motor3.accelerate()
        Motor4.accelerate()
    else:
        center()

    if (
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 0) and (SensorIn_5.value() == 1))
    ):  
        center()
        sleep(0.2)
        Motor1.reverse()
        Motor2.reverse()
        Motor3.reverse()
        Motor4.reverse()

    debug_time = ticks_diff(ticks_ms(), debug_timer1)
    debug_list.append(debug_time)
    startTime = ticks_ms()
    while(((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1))):
        if (ticks_diff(ticks_ms(), startTime)/1000 > 5):
            Motor1.stop()
            Motor2.stop()
            Motor3.stop()
            Motor4.stop()    
            turn_left()
            turn_right()
            turn_left()
            turn_right()
            flag = False
            break


#Exit protocol
freq(80000000)
center()
MotorPins.setOutputs([0,0,0,0,0,0,0,0])
MotorPins.latch()
print(debug_list)