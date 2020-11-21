#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import MySQLdb
import json
import datetime

print ('PythonFiles 0.2')
print ('')
print (' ,_ o')
print ('/ //\,')
print (' \>> |')
print ('  \\,')
print ('Created by: Alex Biglen')
print ('Date: 03/15/2019')

#----Variables----
#Set Date/Time program began
startDateTime = datetime.datetime.now()
lightSensorStatus = GPIO.input(17)


#----File connections----
#LogFile
l = open("/Shared/Logs/log.txt","a")
l.write(str(startDateTime))
l.write("Logging file active")
#DumpFile
d = open("/Shared/Dump/dump.txt","a")


#----Database connection----
conn = MySQLdb.connect(
host="",
user="",
passwd="",
db="")
x= conn.cursor()
try:
    x.execute("SELECT * FROM %DATABASENAMEHERE%")
	conn.commit()
except:
    conn.rollback()
	
#----Python Obj to json----
pythonObj = {
 "TempCelc": temperature,
 "TempFaren": convertToF,
 "Humidity":humidity,
 "LightStatus": lightSensorStatus
}
#execute conversion:
jsonData = json.dumps(pythonObj)
#print out JSON String:
print(jsonData)


#----Main Program Execution loop----
while True:

    GPIO.setmode(GPIO.BCM)
	#Set GPIO Data Pin from DHT11
    GPIO.setup(17,GPIO.IN)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    convertToF = temperature*1.8+32
	
	#Outputs:
	print (str(startDateTime))
    print ('Temp: {0:0.1f} C'.format(temperature))
    print ('Temp: {0:0.1f} F, Humidity: {1:0.1f} %'.format(convertToF, humidity)
    print ('Light status: {}'.format(lightSensorStatus)

    #Testing:
    print ('DEBUG: lightSensorStatus Variable string below?')
    print ('DEBUG: ' + lightSensorStatus)
    print ('DEBUG: ')