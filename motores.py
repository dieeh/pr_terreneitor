from machine import Pin, PWM
from time import sleep


class Motor:
    pwm_f = None
    pwm_b = None
    type_pow = ""

    def __init__(self, pin_1: Pin, pin_2: Pin, pow: str, freq=1000, duty=400):
        self.pin_forward = pin_1
        self.pin_backward = pin_2
        self.freq = freq
        self.duty = duty
        if pow == "lin" or pow == "pwm":
            self.type_pow = pow
        else:
            self.type_pow == "lin"
        if self.type_pow == "pwm":
            self.pwm_f = PWM(pin_forward, freq=freq)
            self.pwm_b = PWM(pin_backward, freq=freq)

    def accelerate(freq, duty):
        if self.type_pow == "lin":
            return self.pin_forward.on()
        else:
            self.pwm_f.duty(duty)
            sleep(0.15)
            return

    def reverse():
        if self.type_pow == "lin":
            return self.pin_backward.on()
        else:
            self.pwm_b.duty(duty)
            sleep(0.15)
            return


class Servo:

    def __init__(self, pin: Pin, freq=40, min=15, max=135):
        self.pin = pin
        self.freq = freq
        self.min = min
        self.max = max
        self.motor = PWM(self.pin, freq=freq)

    def movement(angle):
        if (angle >= min) and (angle <= max):
            motor.duty(angle)
            sleep(0.2)


def track_mode():

    return


def rc_mode():
    return
