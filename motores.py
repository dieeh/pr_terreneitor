from machine import Pin, PWM
from time import sleep


def p_to_duty(percentage):
    return round((1023 * percentage) / 100)


class Motor:

    def __init__(self, pin_pwm, pin_forward, pin_backward, freq=500, duty_per=100):
        self.pin_pwm = pin_pwm
        self.pin_forward = pin_forward
        self.pin_backward = pin_backward
        self.freq = freq
        self.duty_per = duty_per
        self.pwm = PWM(self.pin_pwm, freq=self.freq)

    @staticmethod
    def accelerate(duty=self.duty_per):
        self.pin_forward.on()
        self.pin_backward.off()
        self.pwm(p_to_duty(duty))

    @staticmethod
    def reverse(duty=self.duty_per):
        self.pin_forward.off()
        self.pin_backward.on()
        self.pwm(p_to_duty(duty))

    @staticmethod
    def stop():
        self.pin_forward.off()
        self.pin_backward.off()
        self.pwm(0)


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
