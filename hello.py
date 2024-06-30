from machine import Pin, freq
from time import sleep, ticks_ms, ticks_diff
from motor import DCMotor, ServoMotor
from register import ShiftRegister

print('1')
freq(160000000) # Boost CPU frequency to 160MHz -> Better performance
### pin assignments
