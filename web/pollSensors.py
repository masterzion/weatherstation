import requests
import hashlib
import time

#Dont forget to fill in PASSWORD and URL TO saveTemp (twice) in this file

sensorids = ["28-000004eb4e02", "28-000004eb6805"]
avgtemperatures = []
for sensor in range(len(sensorids)):
        temperatures = []
        for polltime in range(0,3):
                text = '';
                while text.split("\n")[0].find("YES") == -1:
                        # Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before.
                        tfile = open("/sys/bus/w1/devices/"+ sensorids[sensor] +"/w1_slave")
                        # Read all of the text in the file.
                        text = tfile.read()
                        # Close the file now that the text has been read.
                        tfile.close()
                        time.sleep(1)

                # Split the text with new lines (\n) and select the second line.
                secondline = text.split("\n")[1]
                # Split the line into words, referring to the spaces, and select the 10th word (counting from 0).
                temperaturedata = secondline.split(" ")[9]
                # The first two characters are "t=", so get rid of those and convert the temperature from a string to a number.
                temperature = float(temperaturedata[2:])
                # Put the decimal point in the right place and display it.
                temperatures.append(temperature / 1000)

        avgtemperatures.append(sum(temperatures) / float(len(temperatures)))

print avgtemperatures[0]
print avgtemperatures[1]

session = requests.Session()
nonce = session.get(url='URL TO saveTemp.php?step=nonce').text

response = hashlib.sha256(nonce + 'PASSWORD' + str(avgtemperatures[0]) + str(avgtemperatures[1])).hexdigest()

post_data = {'response':response, 'temp1':avgtemperatures[0], 'temp2': avgtemperatures[1]}

post_request = session.post(url='URL TO saveTemp.php', data=post_data)

if post_request.status_code == 200 :
        print post_request.text
