# weatherstation

Based in this tutorial:
https://iada.nl/en/blog/article/temperature-monitoring-raspberry-pi


INSTALL
``` bash
apt-get install python-setuptools git sqlite3 python-smbus i2c-tools

echo i2c-dev >> /etc/modules
modprobe i2c-dev

easy_install pip
pip install tornado w1thermsensor

git clone https://github.com/masterzion/weatherstation.git
cd weatherstation
``` 

add this line in  /boot/config.txt
``` ini
dtoverlay=w1-gpio
```



add the crontabfile content in your crontab and reboot


Using: 

Tornado (REST): http://www.tornadoweb.org/en/stable/

Google Charts: https://developers.google.com/chart/



Online Sample:

http://masterzion.no-ip.org:8888/
