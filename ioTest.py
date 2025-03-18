import time
from machine import Pin
import rp2
import random


# pin behavior
p25 = Pin(25, Pin.OUT)
p0 = Pin(0, Pin.IN, Pin.PULL_DOWN)
p1 = Pin(1, Pin.IN, Pin.PULL_DOWN)
p2 = Pin(2, Pin.IN, Pin.PULL_DOWN)

while(1):
    
    # check pin condition value
    v = 0
    
    # blink green LED
    p25.on()
    time.sleep(1)
    p25.off()
    
    # get random number
    x = random.randint(0,2)
    print(x)
    time.sleep(1)
    
    # get value from pin 0
    if(x == 0):
        while(v == 0):
            v = p0.value()
            time.sleep(1)
            
    # get value from pin 1
    elif(x == 1):
        while(v == 0):
            v = p1.value()
            time.sleep(1)
            
    # get value from pin 2
    elif(x == 2):
        while(v == 0):
            v = p2.value()
            time.sleep(1)
            
            
    