from machine import Pin, freq
from time import sleep, ticks_ms, ticks_diff
from motor import DCMotor, ServoMotor


print('start')
freq(240000000) # Boost CPU frequency to 160MHz -> Better performance
### pin assignments

# ESP32-WROOM-32 IO PINS
# GPIO0   -- Not used
# GPIO1   -- Not used
# GPIO2   -- Not used
# GPIO3   -- Not used
# GPIO4   -> DCMotor4_Speed    -> PWM OUTPUT
# GPIO5   -- Not used
# GPIO12  -- Not used
# GPIO13  -> DCMotor3_Speed    -> PWM OUTPUT
# GPIO14  -- Not used
# GPIO15  -- Not used
# GPIO16  -> DCMotor4_Forward  -> OUTPUT-- Not used
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



Motor1 = DCMotor(22, 33, 25, 500)  ## Arrangement of motors
Motor2 = DCMotor(23, 26, 27, 500)  ## --front--
Motor3 = DCMotor(13, 19, 18, 500)  ## M1 - M2
Motor4 = DCMotor(4, 16, 17, 500)    ## M3 - M4
Servo = ServoMotor(21)

print('2')
def turn_right(inv=False):
    if inv:
        Servo.movement(35)
    else:
        Servo.movement(145)


def turn_left(inv=False):
    if inv:
        Servo.movement(145)
    else:
        Servo.movement(35)


def center():
    Servo.movement(90)

def movement(valor: bool):
    if valor:
        Motor1.forward()
        Motor2.forward()
        Motor3.forward()
        Motor4.forward()
    else:
        Motor1.backward() 
        Motor2.backward()
        Motor3.backward()
        Motor4.backward()


SensorIn_1 = Pin(36, Pin.IN, value=0)
SensorIn_2 = Pin(39, Pin.IN, value=0)  ## Arrangement of sensors
SensorIn_3 = Pin(34, Pin.IN, value=0)  ## -- front --
SensorIn_4 = Pin(35, Pin.IN, value=0)  ## 1,2,3,4,5
SensorIn_5 = Pin(32, Pin.IN, value=0)  ## values: 0 for black, 1 for white
debug_list = []
duty_percent = 75
flag_main = True
flag_acc = False
flag_back = False
timer = float('-inf')
center()
while flag_main:
    #debug_timer1 = ticks_ms()
    Motor1.accelerate(duty_percent)
    Motor2.accelerate(duty_percent)
    Motor3.accelerate(duty_percent)
    Motor4.accelerate(duty_percent)
    while (
        (SensorIn_3.value() == 0)
    ):
        movement(True)
        sleep(0.1) 
        center()
        flag_acc = True
        flag_back = False
        print('centro')

    S1, S2, S4, S5 = SensorIn_1.value(), SensorIn_2.value(), SensorIn_4.value(), SensorIn_5.value()
    print(S1, S2, S4, S5)
    if (
        ((S1 == 1) or (S2 == 1)) and ((S4 == 0) or (S5 == 0))
    ):
        if flag_acc:
            movement(True)
            sleep(0.1)
            turn_right()
        else:
            movement(False)
            sleep(0.1)
            turn_left()
    elif (
        ((S1 == 0) or (S2 == 0)) and ((S4 == 1) or (S5 == 1))
    ):
        if flag_acc:
            movement(True)
            sleep(0.1)
            turn_left()
        else:
            movement(False)
            sleep(0.1)
            turn_left()
                                                                              b  
    if flag_acc:
        timer = ticks_ms()
    Motor1.accelerate(70)
    Motor2.accelerate(70)
    Motor3.accelerate(70)
    Motor4.accelerate(70)
    sleep(0.1) 
    movement(False)
    center()
    if ((ticks_diff(ticks_ms(), timer)/1000)>5):
        flag_acc = False
        flag_back = True 
        timer = float('-inf')


            
    #debug_time = ticks_diff(ticks_ms(), debug_timer1)
    #debug_list.append((debug_time/1000))
    #startTime = ticks_ms()
    #while(((SensorIn_1.value() == 1) and (SensorIn_2.value() == 1) and (SensorIn_3.value() == 1) and (SensorIn_4.value() == 1) and (SensorIn_5.value() == 1))):
    #    center()
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
print(debug_list)