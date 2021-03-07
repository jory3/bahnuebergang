# Railway Crossing
Railway crossing: 2 red LEDs and Sound

Note: I am just beginning with Raspberry Pi and Python, this project is not meant to be perfect. 

## Material
- Raspberry Pi Zero WH
- 3W Mono Amp HAT (https://shop.pimoroni.com/products/audio-amp-shim-3w-mono-amp)
- 3W Speaker (https://www.conrad.ch/de/p/visaton-k-50-2-zoll-5-cm-kleinlautsprecher-2-w-50-1173561.html)
- 2 LED and resistors
- 3D-Printer
- push button

## Preparing the Raspberry

Install audio player
```
pip install python-vlc
# or
pip3 install python-vlc
```

add two lines to /boot/config.txt:
```
dtoverlay=hifiberry-dac
gpio=25=op,dh
```

commend this line out in /boot/config.txt:
```
# dtparam=audio=on
```
(See https://shop.pimoroni.com/products/audio-amp-shim-3w-mono-amp for details)

GPIOzero:
```
sudo apt install python3-gpiozero
```

# Pi Connectors
- PIN 6: GND
- Pin 11 / GPIO 17: LED 1
- Pin 13 / GPIO 27: LED 2
- GPIO 18, 19, 21: Used by Audio Amp Shim
- PINs 1 + 21: Switch

## Setup
- Checkout files to /home/pi/projects/bahnuebergang
- install service: 
````
sudo sh /home/pi/projects/bahnuebergang/install_service.sh
````
