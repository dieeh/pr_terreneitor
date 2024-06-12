from machine import Pin, PWM, ADC
from time import sleep
# Sensor ::: valores: blanco = 1, negro = 0
    # Nota el sensor necesita mucho contraste


#sensor = PWM(Pin(5, Pin.OUT), freq=50)
### 15 <= duty <= 135  -> freq = 50
#
#for j in range(2):
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
#sleep(5)
#sensor.duty(135)


pin_1 = Pin(4, Pin.OUT)
pin_2 = Pin(5, Pin.OUT)
#
#for i in range(50):
#  pin_1.on()
#  sleep(0.1)

pin_motor = PWM(pin_1, freq=1000)

for i in range(340, 800, 5):
  pin_motor.duty(i)
  sleep(0.2)
  print(i)

# for i in range(1, 30):
#   pin_motor.duty(400)
#   sleep(0.2)