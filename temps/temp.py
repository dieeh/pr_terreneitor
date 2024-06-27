from machine import Pin, PWM
from time import sleep
from motores import p_to_duty
from Register import ShiftRegister

#
# k = PWM(Pin(14, Pin.OUT), freq=1000)
# j = Pin(5, Pin.OUT)
# w = PWM(Pin(12, Pin.OUT), freq=1000)
# q = Pin(2, Pin.OUT)
#
#
# per = 90
# asd = round((65535 * per) / 100)
#
# for z in range(4):
#    j.on()
#    k.duty_u16(asd)
#    q.on()
#    w.duty_u16(asd)
#    for i in range(5):
#        sleep(0.5)
#    sleep(2)

# Pin1_R = Pin(5,Pin.OUT)
# Pin1_L = Pin(0,Pin.OUT)
# Pin2_R = Pin(2,Pin.OUT)
# Pin2_L = Pin(13,Pin.OUT)
#
# Pin_PWM1R = PWM(Pin1_R, freq=1000)
# Pin_PWM1L = PWM(Pin1_L, freq=1000)
# Pin_PWM2R = PWM(Pin2_R, freq=1000)
# Pin_PWM2L = PWM(Pin2_L, freq=1000)
#
# Pin_dir1R = Pin(4, Pin.OUT)
# Pin_dir1L = Pin(16, Pin.OUT)
# Pin_dir2R = Pin(14, Pin.OUT)
# Pin_dir2L = Pin(15, Pin.OUT)
#
# Pin_dir1R.on()
# Pin_dir1L.on()
# Pin_dir2R.on()
# Pin_dir2L.on()
#
# for i in range(4):
#    for j in range(0,105,5):
#        print(j)
#        Pin_PWM1R.duty(p_to_duty(j))
#        Pin_PWM1L.duty(p_to_duty(j))
#        Pin_PWM2R.duty(p_to_duty(j))
#        Pin_PWM2L.duty(p_to_duty(j))
#        sleep(1)
#    sleep(5)
#    Pin_PWM1R.duty(0)
#    Pin_PWM1L.duty(0)
#    Pin_PWM2R.duty(0)
#    Pin_PWM2L.duty(0)
#
#    sleep(2)


a = ShiftRegister(5, 4, 14, 1)
flag = True

alltrue = [1, 1, 1, 1, 1, 1, 1, 1]
allfalse = [0, 0, 0, 0, 0, 0, 0, 0]

a.setOutputs(alltrue)
a.latch()
print("alltrue")

sleep(2)

a.setOutputs(allfalse)
a.latch()
print("allfalse")


sleep(2)
for j in range(8):
    a.setOutput(j, True)
    a.latch()
    print(f"{j}, on")
    sleep(1)

sleep(2)
for k in range(8):
    a.setOutput(k, False)
    a.latch()
    print(f"{j}, off")
    sleep(1)

# for i in range(3):
#
#    a.setOutput(0, True)
#    print("1")
#    a.latch()
#
#    sleep(2)
#
#    a.setOutput(0, False)
#    print("0")
#    a.latch()
#
#    sleep(2)

#    if flag:
#        a.setOutput(0, True)
#        print("1")
#        a.latch()
#        sleep(2)
#        print('latch1')
#        sleep(2)
#        a.latch()
#        print('latch2')
#        flag = False
