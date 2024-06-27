from machine import Pin, PWM
from time import sleep
from register import ShiftRegister


class DCMotor:

    def __init__(self, shift_register, pin_forward, pin_backward):  # -> Any:
        self.pin_forward = pin_forward
        self.pin_backward = pin_backward
        self.shift_register = shift_register

    def accelerate(self):  # -> Any:
        self.shift_register.setOutput(pin_forward, True)
        self.shift_register.setOutput(pin_backward, False)
        self.shift_register.latch()

    def reverse(self):  # -> Any:
        self.shift_register.setOutput(pin_forward, False)
        self.shift_register.setOutput(pin_backward, True)
        self.shift_register.latch()

    def stop(self):  # -> Any:
        self.shift_register.setOutput(pin_forward, False)
        self.shift_register.setOutput(pin_backward, False)
        self.shift_register.latch()


class ServoMotor:

    def __init__(self, pin_pwm, freq=50, min=0, max=180):  # -> Any:
        self.pin_pwm = Pin(pin_pwm, Pin.OUT)
        self.freq = freq
        self.min = min
        self.max = max
        self.motor = PWM(self.pin_pwm, freq=self.freq)

    def movement(self, angle):  # -> Any:
        if (angle >= self.min) and (angle <= self.max):
            duty = (
                (12.346 * round(angle) ** 2) + (7777.8 * round(angle)) + 700000
            )  # milisegundos
            duty /= 1000000  # bits
            duty = int(duty * 1023 / 20)
            self.motor.duty(duty)
            sleep(0.2)
