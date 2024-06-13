from machine import Pin, PWM
from time import sleep


def p_to_duty(percentage):
    return round((1023 * percentage) / 100)


class DCMotor:

    def __init__(self, pin_pwm, pin_forward, pin_backward, freq=500, duty_per=100):
        self.pin_pwm = pin_pwm
        self.pin_forward = pin_forward
        self.pin_backward = pin_backward
        self.freq = freq
        self.duty_per = duty_per
        self.pwm = PWM(self.pin_pwm, freq=self.freq)

    def accelerate(self, duty=None):
        if duty is None:
            duty = self.duty_per
        self.pin_forward.on()
        self.pin_backward.off()
        self.pwm.duty(p_to_duty(duty))

    def reverse(self, duty=None):
        if duty is None:
            duty = self.duty_per
        self.pin_forward.off()
        self.pin_backward.on()
        self.pwm.duty(p_to_duty(duty))

    def stop(self):
        self.pin_forward.off()
        self.pin_backward.off()
        self.pwm.duty(0)


class ServoMotor:

    def __init__(self, pin_pwm, freq=40, min=15, max=135):
        self.pin_pwm = pin_pwm
        self.freq = freq
        self.min = min
        self.max = max
        self.motor = PWM(self.pin_pwm, freq=self.freq)

    def movement(self, angle):
        if (angle >= self.min) and (angle <= self.max):
            self.motor.duty(angle)
            sleep(0.2)


# def track_mode():
#    return print("a")


# def rc_mode():
#    return print("a")
