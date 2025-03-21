import time
from machine import Pin, I2C
import rp2
import random
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


# pin behavior
p25 = Pin(25, Pin.OUT) #Board LED

#LCD (2-3)
i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

#Drums (4-6)
drum1 = Pin(4, Pin.IN, Pin.PULL_DOWN) #kick
drum2 = Pin(5, Pin.IN, Pin.PULL_DOWN) #snare
drum3 = Pin(6, Pin.IN, Pin.PULL_DOWN) #hat


#Piano (18-21)
piano1 = Pin(18, Pin.IN, Pin.PULL_DOWN) #key 1
piano2 = Pin(19, Pin.IN, Pin.PULL_DOWN) #key 2
piano3 = Pin(20, Pin.IN, Pin.PULL_DOWN) #key 3
piano4 = Pin(21, Pin.IN, Pin.PULL_DOWN) #key 4


#Guitar (7-10)
guitar1 = Pin(7, Pin.IN, Pin.PULL_DOWN) #string 1
guitar2 = Pin(8, Pin.IN, Pin.PULL_DOWN) #string 2
guitar3 = Pin(9, Pin.IN, Pin.PULL_DOWN) #string 3
guitar4 = Pin(10, Pin.IN, Pin.PULL_DOWN) #string 4


#Speaker (11)
speaker = Pin(11, Pin.IN, Pin.PULL_DOWN)


def greeting():
    
    lcd.clear()
    lcd.move_to(5,0)
    lcd.putstr("Welcome")
    lcd.move_to(1,1)
    lcd.putstr("To Guitar Hero")
    time.sleep(2)
    lcd.clear()
    
def play(text):
    
    lcd.clear()
    lcd.move_to(5,0)
    lcd.putstr("Play")
    lcd.move_to(1,1)
    lcd.putstr(text)
    time.sleep(1)
        

greeting()
while(1):
    lcd.clear()
    # check pin condition value
    w = 0 # correct
    l = 0 # incorrect
    
    # blink green LED
    p25.on()
    time.sleep(1)
    p25.off()
    
    # get random number
    # 0 - drum (2-4)
    # 1 - piano (18-21)
    # 2 - guitar (7-10)
    x = random.randint(0,2)
    print(x)
    time.sleep(1)
    
    # get value for drums
    if(x == 0):
        y = random.randint(0,2)
        if(y == 0):
            play("Kick Drum")
            while(w == 0 or l == 0):
                w = drum1.value()
                l = drum2.value()
                l = drum3.value()
                time.sleep(1)
        elif(y == 1):
            play("Snare Drum")
            while(w == 0 or l == 0):
                l = drum1.value()
                w = drum2.value()
                l = drum3.value()
                time.sleep(1)
        elif(y == 2):
            play("Hat Drum")
            while(w == 0 or l == 0):
                l = drum1.value()
                l = drum2.value()
                w = drum3.value()
                time.sleep(1)
            
    # get value for piano
    elif(x == 1):
        y = random.randint(0,3)
        if(y == 0):
            play("Piano Key 1")
            while(w == 0 or l == 0):
                w = piano1.value()
                l = piano2.value()
                l = piano3.value()
                l = piano4.value()
                time.sleep(1)
        elif(y == 1):
            play("Piano Key 2")
            while(w == 0 or l == 0):
                l = piano1.value()
                w = piano2.value()
                l = piano3.value()
                l = piano4.value()
                time.sleep(1)
        elif(y == 2):
            play("Piano Key 3")
            while(w == 0 or l == 0):
                l = piano1.value()
                l = piano2.value()
                w = piano3.value()
                l = piano4.value()
                time.sleep(1)
        elif(y == 3):
            play("Piano Key 4")
            while(w == 0 or l == 0):
                l = piano1.value()
                l = piano2.value()
                l = piano3.value()
                w = piano4.value()
                time.sleep(1)
            
    # get value for guitar
    elif(x == 2):
        y = random.randint(0,3)
        if(y == 0):
            play("Guitar String 1")
            while(w == 0 or l == 0):
                w = guitar1.value()
                l = guitar2.value()
                l = guitar3.value()
                l = guitar4.value()
                time.sleep(1)
        elif(y == 1):
            play("Guitar String 2")
            while(w == 0 or l == 0):
                l = guitar1.value()
                w = guitar2.value()
                l = guitar3.value()
                l = guitar4.value()
                time.sleep(1)
        elif(y == 2):
            play("Guitar String 3")
            while(w == 0 or l == 0):
                l = guitar1.value()
                l = guitar2.value()
                w = guitar3.value()
                l = guitar4.value()
                time.sleep(1)
        elif(y == 3):
            play("Guitar String 4")
            while(w == 0 or l == 0):
                l = guitar1.value()
                l = guitar2.value()
                l = guitar3.value()
                w = guitar4.value()
                time.sleep(1)


