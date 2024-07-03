from machine import Pin, freq
from time import sleep, ticks_ms, ticks_diff
from motor import DCMotor, ServoMotor


print('1')
freq(240000000) # Boost CPU frequency to 160MHz -> Better performance
### pin assignments

# ESP32-WROOM-32 IO PINS
# GPIO0   -- Not used
# GPIO1   -- Not used
# GPIO2   -- Not used
# GPIO3   -- Not used
# GPIO4   -> DCMotor4_Speed    -> PWM OUTPUT
# GPIO5   -> DCMotor4_Forward  -> OUTPUT
# GPIO12  -- Not used
# GPIO13  -> DCMotor3_Speed    -> PWM OUTPUT
# GPIO14  -- Not used
# GPIO15  -- Not used
# GPIO16  -- Not used
# GPIO17  -> DCMotor4_Backward -> OUTPUT
# GPIO18  -> DCMotor3_Backward -> OUTPUT
# GPIO19  -> DCMotor3_Forward  -> OUTPUT
# GPIO21  -> ServoMotor        -> PWM OUTPUT
# GPIO22  -> DCMotor1_Speed    -> PWM OUTPUT
# GPIO23  -> DCMotor2_Speed    -> PWM OUTPUT
# GPIO25  -> DCMotor1_Backward -> OUTPUT
# GPIO26  -> DCMotor2_Forward  -> OUTPUT
# GPIO27  -> DCMotor2_Backward -> OUTPUT
# GPIO32  -> Sensor            -> INPUT
# GPIO33  -> DCMotor1_Forward  -> OUTPUT
# GPIO34  -> Sensor            -> INPUT
# GPIO35  -> Sensor            -> INPUT
# GPIO36  -> Sensor            -> INPUT
# GPIO39  -> Sensor            -> INPUT



Motor1 = DCMotor(22, 33, 25)  ## Arrangement of motors
Motor2 = DCMotor(23, 26, 27)  ## --front--
Motor3 = DCMotor(13, 19, 18)  ## M1 - M2
Motor4 = DCMotor(4, 5, 17)    ## M3 - M4
Servo = ServoMotor(21)

print('2')
def turn_right(inv=False):
    if inv:
        Servo.movement(35)
        sleep(0.2)
        Servo.movement(35)
    else:
        Servo.movement(145)
        sleep(0.2)
        Servo.movement(145)


def turn_left(inv=False):
    if inv:
        Servo.movement(145)
        sleep(0.2)
        Servo.movement(145)
    else:
        Servo.movement(35)
        sleep(0.2)
        Servo.movement(35)


def center():
    Servo.movement(90)
    sleep(0.2)
    Servo.movement(90)


SensorIn_1 = Pin(36, Pin.IN, value=0)
SensorIn_2 = Pin(39, Pin.IN, value=0)  ## Arrangement of sensors
SensorIn_3 = Pin(34, Pin.IN, value=0)  ## -- front --
SensorIn_4 = Pin(35, Pin.IN, value=0)  ## 1,2,3,4,5
SensorIn_5 = Pin(32, Pin.IN, value=0)  ## values: 0 for black, 1 for white
print('3')
debug_list = []
duty_percent = 70
flag_main = True
flag_acc = False
flag_rev = False
flag_right = False
flag_left = False
while flag_main:
    debug_timer1 = ticks_ms()
    S1, S2, S3, S4, S5 = SensorIn_1.value(), SensorIn_2.value(), SensorIn_3.value(), SensorIn_4.value(), SensorIn_5.value()
    print(S1, S2, S3, S4, S5)
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
        if flag_acc == False:
            Motor1.stop()
            Motor2.backward()
            Motor3.forward()
            Motor4.backward()
            flag_acc = True
            flag_rev = False
        Motor1.accelerate(duty_percent)
        Motor2.accelerate(duty_percent)
        Motor3.accelerate(duty_percent)
        Motor4.accelerate(duty_percent)
        print('s')
        print(Motor1.debug())
        print(Motor2.debug())
        print(Motor3.debug())
        print(Motor4.debug())
        sleep(0.2)
    elif (
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
        #if flag_right == False:
        #    Motor1.accelerate()
        #    Motor2.stop()
        #    Motor3.accelerate()
        #    Motor4.accelerate()
        #    flag_right = True
        #    flag_left = False
    #else:
    #    center()

    elif (
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
       # if flag_left == False:
       #     Motor1.stop()
       #     Motor2.accelerate()
       #     Motor3.accelerate()
       #     Motor4.accelerate()
       #     flag_left = True
       #     flag_right = False
    #else:
    #    center()

    elif (
        ((S1 == 0) and (S2 == 0) and (S3 == 0) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 0) and (S2 == 0) and (S3 == 0) and (S4 == 0) and (S5 == 1)) or 
        ((S1 == 0) and (S2 == 0) and (S3 == 1) and (S4 == 0) and (S5 == 0)) or 
        ((S1 == 0) and (S2 == 0) and (S3 == 1) and (S4 == 0) and (S5 == 1))
    ):  
        center()
        sleep(0.2)
        if flag_rev == False:
            print('a')
            Motor1.backward() 
            Motor2.forward()
            Motor3.backward()
            Motor4.forward()
            flag_rev = True
            flag_acc = False
        Motor1.accelerate(duty_percent)
        Motor2.accelerate(duty_percent)
        Motor3.accelerate(duty_percent)
        Motor4.accelerate(duty_percent)
        print('r')
        print(Motor1.debug())
        print(Motor2.debug())
        print(Motor3.debug())
        print(Motor4.debug())
        sleep(0.2)

            
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
            flag_main = False
            break


#Exit protocol
freq(160000000)
center()
print(debug_list)