from machine import Pin, PWM
from time import sleep
import time


# Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(0))

# Set the PWM frequency.
pwm.freq(247)

# Play C4
duty = 0
direction = 1
for _ in range(2 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
    
pwm.freq(220)

# Play D4
duty = 0
direction = 1
for _ in range(2 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
    
pwm.freq(196)

# Play E4
duty = 0
direction = 1
for _ in range(2 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)

time.sleep(0.5)
    
pwm.freq(247)

# Play C4
duty = 0
direction = 1
for _ in range(2 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
    
pwm.freq(220)

# Play D4
duty = 0
direction = 1
for _ in range(2 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
    
pwm.freq(196)

# Play E4
duty = 0
direction = 1
for _ in range(2 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)

time.sleep(0.5)

pwm.freq(196)

# Play E4
duty = 0
direction = 1
for _ in range(1 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
duty = 0
direction = 1
for _ in range(1 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
duty = 0
direction = 1
for _ in range(1 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
duty = 0
direction = 1
for _ in range(1 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)

pwm.freq(220)
duty = 0
direction = 1
for _ in range(1 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
duty = 0
direction = 1
for _ in range(1 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
duty = 0
direction = 1
for _ in range(1 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
duty = 0
direction = 1
for _ in range(1 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
    
pwm.freq(247)

# Play C4
duty = 0
direction = 1
for _ in range(2 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
    
pwm.freq(220)

# Play D4
duty = 0
direction = 1
for _ in range(2 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
    
pwm.freq(196)

# Play E4
duty = 0
direction = 1
for _ in range(2 * 256):
#while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)