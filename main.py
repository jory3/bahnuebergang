#!/usr/bin/python
import RPi.GPIO as GPIO
import time, sys
from gpiozero import LED
from time import sleep
import vlc

led = LED(27)
led2 = LED(17)
readysound = vlc.MediaPlayer("/home/pi/projects/bahnuebergang/ding.wav")

# Use Pin Numbers, not GPIO numbers
# GPIO.setmode(GPIO.BOARD)

GPIO.setup(9, GPIO.IN)

def switch_on(pin):
    global led, led2
    p = vlc.MediaPlayer("/home/pi/projects/bahnuebergang/barriere.wav")
    p.play()
    print("go")

    i = 0
    while i < 13:
        led.on()
        led2.off()
        sleep(1)
        led2.on()
        led.off()
        sleep(1)
        i = i+1
    led2.off()
    return

GPIO.add_event_detect(9, GPIO.FALLING, bouncetime=32*1000)
GPIO.add_event_callback(9, switch_on)

readysound.play()
led.on()
led2.on()
sleep(1.5)
led.off()
led2.off()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()

