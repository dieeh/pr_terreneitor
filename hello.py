from machine import Pin, freq
from time import sleep, ticks_ms, ticks_diff
from motor import DCMotor, ServoMotor
from register import ShiftRegister

print('1')
freq(80000000) # Boost CPU frequency to 160MHz -> Better performance
### pin assignments



k = ShiftRegister(0, 2, 13)

k.setOutputs([0,0,0,0,0,0,0,0])
k.latch()



k.setOutputs([1,0,1,0,1,0,1,0])
k.latch()

for i in range(10):
    sleep(1)
    print(f"{i+1} segundo")
    print(f"valor pin io0 {Pin(0).value()}")
    print(f"valor pin io2 {Pin(2).value()}")
    print(f"valor pin io13 {Pin(13).value()}")
    if (((i+1)%2) == 0):
        k.setOutputs([1,0,1,0,1,0,1,0])
        k.latch()

k.setOutputs([0,0,0,0,0,0,0,0])
k.latch()
sleep(2)
k.setOutputs([0,0,0,0,0,0,0,0])
k.latch()