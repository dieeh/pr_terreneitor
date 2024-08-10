from machine import Pin, freq
from time import sleep, ticks_ms, ticks_diff
from motor import DCMotor, ServoMotor
#from register import ShiftRegister

freq(240000000) # Boost CPU frequency to 160MHz -> Better performance

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

#MotorPins = ShiftRegister(0, 2, 13)  ## Init Register
#MotorPins.setOutputs([0,0,0,0,0,0,0,0])  
#MotorPins.latch()

Motor1 = DCMotor(22, 33, 25)  ## Arrangement of motors
Motor2 = DCMotor(23, 26, 27)  ## --front--
Motor3 = DCMotor(13, 19, 18)  ## M1 - M2
Motor4 = DCMotor(4, 16, 17)    ## M3 - M4
Servo = ServoMotor(21)


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


SensorIn_1 = Pin(36, Pin.IN, value=0)
SensorIn_2 = Pin(39, Pin.IN, value=0)  ## Arrangement of sensors
SensorIn_3 = Pin(34, Pin.IN, value=0)  ## -- front --
SensorIn_4 = Pin(35, Pin.IN, value=0)  ## 1,2,3,4,5
SensorIn_5 = Pin(32, Pin.IN, value=0)  ## values: 0 for black, 1 for white

debug_list = []
duty_percent = 77
flag_main = True
while flag_main:
    debug_timer1 = ticks_ms()
    if (
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 0) and (SensorIn_4.value() == 0)) or 
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 0) and (SensorIn_4.value() == 1))
    ):
        Motor1.forward()
        Motor2.forward()
        Motor3.forward()
        Motor4.forward()
        Motor1.accelerate(duty_percent)
        Motor2.accelerate(duty_percent)
        Motor3.accelerate(duty_percent)
        Motor4.accelerate(duty_percent)
        sleep(0.2)

    if (
        ((SensorIn_2.value() == 1) and (SensorIn_4.value() == 0)) or ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 0))
    ):
        
        turn_right()
        for i in range(2):
            Motor1.accelerate(duty_percent)
            Motor2.accelerate(0)
            Motor3.accelerate(duty_percent)
            Motor4.accelerate(15)
            sleep(0.3)
            Motor4.backward()
            Motor3.forward()

            sleep(0.5)
        # sleep(0.2)

    else:
        center()

    if (
        ((SensorIn_2.value() == 0) and (SensorIn_4.value() == 1)) or 
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1))
    ):
        turn_left()
        Motor1.accelerate(0)
        Motor2.accelerate(duty_percent)
        Motor3.accelerate(0)
        Motor4.accelerate(duty_percent)
        sleep(0.2)
    else:
        center()

    if (
        ((SensorIn_1.value() == 0) and (SensorIn_2.value() == 0) and (SensorIn_4.value() == 0)) or
        ((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1))
    ):  
        center()
        Motor1.backward() 
        Motor2.backward()
        Motor3.backward()
        Motor4.backward()
        Motor1.accelerate(duty_percent)
        Motor2.accelerate(duty_percent)
        Motor3.accelerate(duty_percent)
        Motor4.accelerate(duty_percent)
        sleep(0.2)

    #debug_time = ticks_diff(ticks_ms(), debug_timer1)
    #debug_list.append((debug_time/1000))
    #startTime = ticks_ms()
    #while(((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1))):
    #    if (ticks_diff(ticks_ms(), startTime)/1000 > 3):
    #        Motor1.stop()
    #        Motor2.stop()
    #        Motor3.stop()
    #        Motor4.stop()    
    #        turn_left()
    #        turn_right()
    #        turn_left()
    #        turn_right()
    #        flag_main = False
    #        break


#Exit protocol
freq(160000000)
center()
#MotorPins.setOutputs([0,0,0,0,0,0,0,0])
#MotorPins.latch()
print(debug_list)