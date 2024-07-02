from machine import Pin, freq
from time import sleep, ticks_ms, ticks_diff
from motor import DCMotor, ServoMotor
from register import ShiftRegister

print('1')
freq(160000000) # Boost CPU frequency to 160MHz -> Better performance
### pin assignments

# ESP8266 IO PINS
# D0 -> GPIO16  -> Sensor -> INPUT
# D1 -> GPIO5   -> Sensor -> INPUT
# D2 -> GPIO4   -> Sensor -> INPUT
# D3 -> GPIO0   -> Register -> OUTPUT
# D4 -> GPIO2   -> Register -> OUTPUT
# D5 -> GPIO14  -> Sensor -> INPUT
# D6 -> GPIO12  -> Sensor -> INPUT
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

MotorPins = ShiftRegister(0, 2, 13)  ## Init Register
MotorPins.setOutputs([0,0,0,0,0,0,0,0])  
MotorPins.latch()

Motor1 = DCMotor(MotorPins, 0, 1)  ## Arrangement of motors
Motor2 = DCMotor(MotorPins, 2, 3)  ## --front--
Motor3 = DCMotor(MotorPins, 4, 5)  ## M1 - M2
Motor4 = DCMotor(MotorPins, 6, 7)  ## M3 - M4
Servo = ServoMotor(15)

print('2')
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
SensorIn_4 = Pin(14, Pin.IN, value=0)  ## 1,2,3,4,5
SensorIn_5 = Pin(12, Pin.IN, value=0)  ## values: 0 for black, 1 for white
print('3')
debug_list = []
flag = True
while flag:
    debug_timer1 = ticks_ms()
    S1, S2, S3, S4, S5 = SensorIn_1.value(), SensorIn_2.value(), SensorIn_3.value(), SensorIn_4.value(), SensorIn_5.value()
    print(S1, S2, S3, S4, S5)
    MotorPins.debug()
    if (
        ((S1 == 0) and (S2 == 1) and (S3 == 0) and (S4 == 1) and (S5 == 0)) or 
        ((S1 == 0) and (S2 == 1) and (S3 == 0) and (S4 == 1) and (S5 == 1)) or 
        ((S1 == 0) and (S2 == 1) and (S3 == 1) and (S4 == 1) and (S5 == 0)) or 
        ((S1 == 1) and (S2 == 0) and (S3 == 0) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 1) and (S2 == 0) and (S3 == 0) and (S4 == 0) and (S5 == 1)) or 
        ((S1 == 1) and (S2 == 0) and (S3 == 1) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 1) and (S2 == 0) and (S3 == 1) and (S4 == 0) and (S5 == 1)) or 
        ((S1 == 1) and (S2 == 1) and (S3 == 0) and (S4 == 1) and (S5 == 0)) or 
        ((S1 == 1) and (S2 == 1) and (S3 == 0) and (S4 == 1) and (S5 == 1))
    ):
        Motor1.accelerate()
        Motor2.accelerate()
        Motor3.accelerate()
        Motor4.accelerate()

    if (
        ((S1 == 0) and (S2 == 1) and (S3 == 0) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 0) and (S2 == 1) and (S3 == 0) and (S4 == 0) and (S5 == 1)) or 
        ((S1 == 0) and (S2 == 1) and (S3 == 1) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 0) and (S2 == 1) and (S3 == 1) and (S4 == 0) and (S5 == 1)) or 
        ((S1 == 1) and (S2 == 1) and (S3 == 0) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 1) and (S2 == 1) and (S3 == 0) and (S4 == 0) and (S5 == 1)) or 
        ((S1 == 1) and (S2 == 1) and (S3 == 1) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 1) and (S2 == 1) and (S3 == 1) and (S4 == 0) and (S5 == 1)) or 
        ((S1 == 1) and (S2 == 1) and (S3 == 1) and (S4 == 1) and (S5 == 0))
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
        ((S1 == 0) and (S2 == 0) and (S3 == 0) and (S4 == 1) and (S5 == 0)) or 
        ((S1 == 0) and (S2 == 0) and (S3 == 0) and (S4 == 1) and (S5 == 1)) or 
        ((S1 == 0) and (S2 == 0) and (S3 == 1) and (S4 == 1) and (S5 == 0)) or 
        ((S1 == 0) and (S2 == 0) and (S3 == 1) and (S4 == 1) and (S5 == 1)) or 
        ((S1 == 0) and (S2 == 1) and (S3 == 1) and (S4 == 1) and (S5 == 1)) or 
        ((S1 == 1) and (S2 == 0) and (S3 == 0) and (S4 == 1) and (S5 == 0)) or 
        ((S1 == 1) and (S2 == 0) and (S3 == 0) and (S4 == 1) and (S5 == 1)) or 
        ((S1 == 1) and (S2 == 0) and (S3 == 1) and (S4 == 1) and (S5 == 0)) or 
        ((S1 == 1) and (S2 == 0) and (S3 == 1) and (S4 == 1) and (S5 == 1))
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
        ((S1 == 0) and (S2 == 0) and (S3 == 0) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 0) and (S2 == 0) and (S3 == 0) and (S4 == 0) and (S5 == 1)) or 
        ((S1 == 0) and (S2 == 0) and (S3 == 1) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 0) and (S2 == 0) and (S3 == 1) and (S4 == 0) and (S5 == 1))
    ):  
        center()
        sleep(0.2)
        print('a')
        Motor1.reverse()
        Motor2.reverse()
        Motor3.reverse()
        Motor4.reverse()
    debug_time = ticks_diff(ticks_ms(), debug_timer1)
    debug_list.append((debug_time/1000))
    startTime = ticks_ms()
    while(((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1))):
        if (ticks_diff(ticks_ms(), startTime)/1000 > 3):
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