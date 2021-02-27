from gpiozero import LED
from time import sleep
import vlc

led = LED(27)
led2 = LED(17)
p = vlc.MediaPlayer("/home/pi/projects/bahnuebergang/sound.mp3")
j = 0

while True:
    p.play()
    i = 0
    j = j+1
    while True:
        led.on()
        sleep(1)
        led2.on()
        led.off()
        sleep(1)
        led2.off()
        i = i+1
        print(i)
        if i > 3:
            break

    p.stop()
    print("stop")
    p.play()
    if j > 3:
        break
