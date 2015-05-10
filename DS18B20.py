import os
import glob
import time
import sqlite3
from time import gmtime, strftime
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

conn = sqlite3.connect('/root/smarthome.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensors (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor int, value real, datetime string )''')

 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
#        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
	
while True:
    sensor_value=read_temp()
    datetime=strftime("%d-%m-%Y %H:%M", time.localtime())
    c.execute("INSERT INTO sensors (sensor, value, datetime)  VALUES (4,"+str(sensor_value)+",'"+datetime+"')")
    conn.commit()
    time.sleep(60)
