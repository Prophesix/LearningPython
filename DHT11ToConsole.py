#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO

while True:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.IN)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print('Temp: {0:0.1f} C'.format(temperature))
    convert = temperature*1.8+32
    print('Temp: {0:0.1f} F Humidity: {1:0.1f} %'.format(convert, humidity))
    print('Light status: {}'.format(GPIO.input(17)))
