from machine import Pin, PWM, ADC
from time import sleep

# Sensor ::: valores: blanco = 1, negro = 0
# Nota el sensor necesita mucho contraste


# sensor = PWM(Pin(5, Pin.OUT), freq=50)
### 15 <= duty <= 135  -> freq = 50
#
# for j in range(2):
#
#   # for i in range(10, 110):
#    #    sensor.duty(i)
#     #   sleep(0.3)
#      #  print(i)
#
#    for h in range(15, 113):
#       sensor.duty(h)
#       sleep(0.01)
#       print(h)
#
#
##sensor.duty(15)
# sleep(5)
# sensor.duty(135)


pin_1 = Pin(5, Pin.OUT)
pin_2 = Pin(2, Pin.OUT)
#
# for i in range(50):
#  pin_1.on()
#  sleep(0.1)

pin_motor1 = PWM(pin_1)
pin_motor2 = PWM(pin_2)
print(pin_motor1.freq())
print(pin_motor2.freq())

# for i in range(1200, 950, 5):
#    pin_motor.duty(i)
#    sleep(0.5)
#    print(i)


per = 70
k = round((65535 * per) / 100)

for i in range(15):
    pin_motor1.duty_u16(k)
    pin_motor2.duty_u16(k)
    sleep(0.2)

# for i in range(1, 30):
#   pin_motor.duty(400)
#   sleep(0.2)
