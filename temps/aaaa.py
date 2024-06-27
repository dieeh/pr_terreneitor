import machine
import time

print(machine.freq())

start1 = time.ticks_ms() # get millisecond counter
i=0
while i < 100000:
    i+=1

delta1 = time.ticks_diff(time.ticks_ms(), start1) # compute time difference


print(f"Total time: {delta1}")


machine.freq(160000000)
print(machine.freq())

start2 = time.ticks_ms() # get millisecond counter
j=0
while j < 100000:
    j+=1

delta2 = time.ticks_diff(time.ticks_ms(), start2) # compute time difference


print(f"Total time: {delta2}")

machine.freq(80000000)

print(f"Diferencia: {(abs(delta2-delta1)/delta1)*100}%")