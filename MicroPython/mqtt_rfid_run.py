#https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
import mfrc522
from os import uname
import machine
import time
from umqtt.simple import MQTTClient
wlan = network.WLAN(network.STA_IF)
while not wlan.isconnected():
    utime.sleep(1)

if uname()[0] == 'WiPy':
elif uname()[0] == 'esp8266':
else:
# def sub_cb(topic, msg):
#     msg = int(msg)
#     print((topic, msg))

SERVER = "10.6.1.112"
ID = "esp"
USER = b"esp"
PASSWORD = b"senhaesp"

c = MQTTClient(ID, SERVER, user=USER, password=PASSWORD)

while True:
	# print("")
	(stat, tag_type) = rdr.request(rdr.REQIDL)
	if stat == rdr.OK:
		(stat, raw_uid) = rdr.anticoll()
		if stat == rdr.OK:
			#print("New card detected")
			for i in range(0, 4):
			# if rdr.select_tag(raw_uid) == rdr.OK:

    #try:
    #c.publish(TOPIC, str(uid))
    #c.publish(TOPIC2, str(hum))
    #c.disconnect()
    #time.sleep(30) #30 segundos
    #finally:
        #c.disconnect()