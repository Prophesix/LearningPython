#!/usr/bin/python
import sys
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

print('PythonFiles 0.1')
print('')
print(' ,_ o')
print('/ //\,')
print(' \>> |')
print('  \\,')
print('Created by: Alex Biglen')
print('Date: 03/15/2019')

GPIO.setmode(GPIO.BCM)
inputChanList = [2, 3]  # Assign Input Channels
outputChanList = []  # Assign Output Channels
GPIO.setup(inputChanList, GPIO.IN)  # Build inputs
GPIO.setup(outputChanList, GPIO.OUT)  # Build Outputs

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 2)  # Adafruit_DHT.read_retry(sensor, DHT_DATA_PIN)
    print('Temp: {0:0.1f} C'.format(temperature))  # Celsius output
    convert = temperature * 1.8 + 32
    print('Temp: {0:0.1f} F Humidity: {1:0.1f} %'.format(convert, humidity))  # Fahrenheit Output and Humidity
    print('Light status: {}'.format(GPIO.input(3)))  # Light status Port 3 Not working?
    time.sleep(5)  # Pause loop for 5 seconds.
