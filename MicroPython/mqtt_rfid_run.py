#https://github.com/micropython/micropython-lib/tree/master/umqtt.simple#https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_pub.py#https://github.com/micropython/micropython-lib/pull/91#issuecomment-239030008
import mfrc522
from os import uname
import machine
import time
from umqtt.simple import MQTTClient
wlan = network.WLAN(network.STA_IF)
while not wlan.isconnected():
    utime.sleep(1)

if uname()[0] == 'WiPy':    rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
elif uname()[0] == 'esp8266':    rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
else:    raise RuntimeError("Unsupported platform")
# def sub_cb(topic, msg):
#     msg = int(msg)
#     print((topic, msg))

SERVER = "10.6.1.112"TOPIC = b"/rfid/normal"
ID = "esp"
USER = b"esp"
PASSWORD = b"senhaesp"

c = MQTTClient(ID, SERVER, user=USER, password=PASSWORD)#c.set_callback(sub_cb)#c.subscribe(TOPICO)

while True:    uid = ""
	# print("")	# print("Place card before reader to read from address 0x08")	# print("")
	(stat, tag_type) = rdr.request(rdr.REQIDL)
	if stat == rdr.OK:
		(stat, raw_uid) = rdr.anticoll()
		if stat == rdr.OK:
			#print("New card detected")			#print("  - tag type: 0x%02x" % tag_type)			#print("%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
			for i in range(0, 4):				uid = uid + "%02x" % raw_uid[i]            uid = uid + "0"            print(uid)            c.connect()            c.publish(TOPIC, b"%s" % uid)            c.disconnect()
			# if rdr.select_tag(raw_uid) == rdr.OK:			#			# 	key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]			#			# 	if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:			# 		print("Address 8 data: %s" % rdr.read(8))			# 		rdr.stop_crypto1()			# 	else:			# 		print("Authentication error")			# else:			# 	print("Failed to select tag")

    #try:    #c.connect()    #d.measure()    #temp = d.temperature()    #hum = d.humidity()    #print('Temp: %s' % temp)    #print('Hum: %s' % hum)
    #c.publish(TOPIC, str(uid))
    #c.publish(TOPIC2, str(hum))
    #c.disconnect()
    #time.sleep(30) #30 segundos
    #finally:
        #c.disconnect()
