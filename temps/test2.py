from machine import Pin, PWM
from time import sleep


def p_to_duty(percentage: int):  # -> Any:
    return round((1023 * percentage) / 100)


x = Pin(5, Pin.OUT)

k = PWM(x, freq=50)  ##RANGO DUTY 17 - 134

# k.duty(122)
# sleep(1)

# for angulo in range(181):
#    print(angulo)

angulo = 90
if angulo >= 0 and angulo <= 180:
    # nanosegundos
    duty = 12.346 * angulo**2 + 7777.8 * angulo + 700000
    # milisegundos
    duty /= 1000000
    # bits
    duty = int(duty * 1023 / 20)
    k.duty(duty)
else:
    print("Digite un ángulo entre 0 y 180")
sleep(0.5)

# for i in range(17, 135):
#    k.duty(i)
#    sleep(1)
#    print(i)
# y = Pin(4, Pin.OUT)

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


# print("1ra dir")
# x.on()
# y.off()
# for i in range(1):
#    sleep(3)
# x.off()
# y.off()
# sleep(3)
# print("2da dir")
# x.off()
# y.on()
# for i in range(1):
#    sleep(3)
# x.off()
# y.off()
def girar(angulo, serv):
    if angulo >= 0 and angulo <= 180:
        # nanosegundos
        duty = 12.346 * angulo**2 + 7777.8 * angulo + 700000
        # milisegundos
        duty /= 1000000
        # bits
        duty = int(duty * 1023 / 20)
        serv.duty(duty)
    else:
        print("Digite un ángulo entre 0 y 180")
    sleep(0.5)

for i in range(5):
    girar(35, k)
    sleep(1)
    girar(90, k)
    sleep(1)
    girar(145, k)
    sleep(1)
    girar(90, k)
    sleep(1)