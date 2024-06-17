from machine import Pin, PWM, ADC
from time import sleep
from motor import DCMotor, ServoMotor
from register import ShiftRegister

### pin assignments

# ESP8266 IO PINS
# D0 -> GPIO16  -> Sensor -> INPUT
# D1 -> GPIO5   -> Register -> OUTPUT
# D2 -> GPIO4   -> Register -> OUTPUT
# D3 -> GPIO0   -> Sensor -> INPUT
# D4 -> GPIO2   -> Sensor -> INPUT
# D5 -> GPIO14  -> Register -> OUTPUT
# D6 -> GPIO12  -> Sensor -> INPUT
# D7 -> GPIO13  -> Sensor -> INPUT
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

MotorPins = ShiftRegister(5, 4, 14)
Motor1 = DCMotor(MotorPins, 0, 1)
Motor2 = DCMotor(MotorPins, 2, 3)
Motor3 = DCMotor(MotorPins, 4, 5)
Motor4 = DCMotor(MotorPins, 6, 7)
Servo = ServoMotor(15)
