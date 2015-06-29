import os

import time
import dhtreader

from time import gmtime, strftime
from w1thermsensor import W1ThermSensor
from models import Sensors


dhtpin=17
dev_type=22

dhtreader.init()


time.sleep(10)

 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
sensor = W1ThermSensor()	
while True:
    try:
        sensor2_value_t, sensor2_value_h = dhtreader.read(dev_type, dhtpin)
        sensor1_value = sensor.get_temperature()
        datetime=strftime("%d-%m-%Y %H:%M", time.localtime())
        Sensors().InsertData(sensor1_value,sensor2_value_t, sensor2_value_h, datetime)
        time.sleep(60)
    except ValueError:
       print "Oops!  That was no valid number.  Try again..."
