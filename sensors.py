import os

import time
import Adafruit_DHT

from time import gmtime, strftime
from w1thermsensor import W1ThermSensor
from models import Sensors


dhtpin=17
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
sensor = W1ThermSensor()	
while True:
    sensor2_value_h, sensor2_value_t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, dhtpin)
    if sensor2_value_t  and sensor2_value_h:
       sensor1_value = sensor.get_temperature()
       datetime=strftime("%d-%m-%Y %H:%M", time.localtime())
       Sensors().InsertData(sensor1_value,sensor2_value_t, sensor2_value_h, datetime)
       time.sleep(60)
    else:
       time.sleep(5)
