import network, utime, machine, ubinascii, json, teste_web0, mqtt_rfid
count = 0

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

preJson = open('config.txt').read()
data = json.loads(preJson)
config = data['campos']

wlan.connect(config[0], config[1])

while not wlan.isconnected():
    utime.sleep(1)
    count = count +1
    if(count == 10):
        wlan.active(False)
        ssid=str(ubinascii.hexlify(wlan.config('mac')))[8:-1]
        ap = network.WLAN(network.AP_IF)
        ap.active(True)
        ap.config(essid='ESP_Config-'+ssid, authmode=network.AUTH_WPA_WPA2_PSK, password='senhafacil'+ssid)
        teste_web0.config()
        wlan.active(True)
        ap.active(False)
        preJson2 = open('config.txt').read()
        data2 = json.loads(preJson2)
        config2 = data2['campos']
        wlan.connect(config2[0], config2[1])
        count = 0

mqtt_rfid.conectar()