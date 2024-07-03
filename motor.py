from machine import Pin, PWM
from time import sleep

def p_to_duty(percentage: int):  # -> Any:
    return round((1023 * percentage) / 100)

class DCMotor:

    def __init__(self, pin_pwm, pin_forward, pin_backward, freq=1000):  # -> Any:
        self.pin_forward = Pin(pin_forward, Pin.OUT)
        self.pin_backward = Pin(pin_backward, Pin.OUT)
        self.freq = freq
        self.pin_pwm = Pin(pin_pwm, Pin.OUT)
        self.pwm = PWM(pin_pwm, freq=self.freq)

    def accelerate(self, percentage):
        self.pwm.duty(p_to_duty(percentage))
    
    def forward(self):  # -> Any:
        self.pin_forward.on()
        self.pin_backward.off()

    def backward(self):  # -> Any:
        self.pin_forward.off()
        self.pin_backward.on()

    def stop(self):  # -> Any:
        self.pin_forward.off()
        self.pin_backward.off()
        self.pwm.duty(0)

    def debug(self):
        return [self.pin_forward.value(), self.pin_backward.value()]


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
