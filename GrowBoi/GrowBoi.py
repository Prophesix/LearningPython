#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO

while True:
    GPIO.setmode(GPIO.BCM)
    inputChanList = [2, 3]  # Assign Input Channels
    outputChanList = []  # Assign Output Channels
    GPIO.setup(inputChanList, GPIO.IN)  # Build inputs
    GPIO.setup(outputChanList, GPIO.OUT)  # Build Outputs

    humidity, temperature = Adafruit_DHT.read_retry(11, 2)  # Adafruit_DHT.read_retry(sensor, DHT_DATA_PIN)
    print('Temp: {0:0.1f} C'.format(temperature))  # Celsius output
    convert = temperature * 1.8 + 32
    print('Temp: {0:0.1f} F Humidity: {1:0.1f} %'.format(convert, humidity))  # Fahrenheit Output and Humidity
    print('Light status: {}'.format(GPIO.input(3)))  #Light status Port 3
