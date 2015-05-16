import os

import time
from time import gmtime, strftime

from w1thermsensor import W1ThermSensor

from models import Sensors

 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
sensor = W1ThermSensor()	
while True:
    sensor1_value = sensor.get_temperature()
    datetime=strftime("%d-%m-%Y %H:%M", time.localtime())
    Sensors().InsertData(sensor1_value, datetime)
    time.sleep(60)
