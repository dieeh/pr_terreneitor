from machine import Pin, PWM
from time import sleep


def p_to_duty(percentage: int):  # -> Any:
    return round((1023 * percentage) / 100)


x = Pin(5, Pin.OUT)
y = Pin(4, Pin.OUT)

# pw = PWM(x, freq=1000)
# print("1ra dir")
# y.on()
# pw.duty(p_to_duty(70))
# for i in range(1):
#    sleep(3)
# pw.duty(0)
# y.off()
# sleep(5)
# print("2da dir")
# pw.duty(p_to_duty(70))
# for i in range(1):
#    sleep(3)
# pw.duty(0)


print("1ra dir")
x.on()
y.off()
for i in range(1):
    sleep(3)
x.off()
y.off()
sleep(3)
print("2da dir")
x.off()
y.on()
for i in range(1):
    sleep(3)
x.off()
y.off()
