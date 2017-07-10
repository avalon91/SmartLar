import network, utime, machine, ubinascii
count = 0

wlan = network.WLAN(network.STA_IF)
while not wlan.isconnected():
    utime.sleep(1)
    count = count +1
    if(count == 10):
        wlan.active(False)
        ap = network.WLAN(network.AP_IF)
        ap.active(True)
        ssid=str(ubinascii.hexlify(wlan.config('mac')))[8:-1]
        ap.config(essid='LAR_Testes-'+ssid, authmode=network.AUTH_WPA_WPA2_PSK, password='senhafacil'+ssid)
