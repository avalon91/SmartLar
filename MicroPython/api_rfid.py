tp2 = 0

def conectar():
    import mfrc522, machine, time, json, utime, urequests
    from os import uname

    lGre = machine.Pin(13, machine.Pin.OUT)
    lRed = machine.Pin(12, machine.Pin.OUT)
    rele = machine.Pin(16, machine.Pin.OUT)
    rele.low()

    rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

    preJson = open('config.txt').read()
    data = json.loads(preJson)
    config = data['campos']

    def check_rfid():
        uid = ""

        (stat, tag_type) = rdr.request(rdr.REQIDL)

        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                for i in range(0, 4):
                    uid = uid + "%02x" % raw_uid[i]
                print(uid)
                # uid = uid + "0"
                # c.publish(TOPIC1, b"%s" % uid)
                lGre.high()
    
    def timeHandler():
        if((rele.value() == True) and (utime.ticks_diff(utime.ticks_ms(), tp2) >= 5000)):
            lGre.low()
            rele.low()
            print('foi')
        elif((lRed.value() == True) and (utime.ticks_diff(utime.ticks_ms(), tp2) >= 2000)):
            lGre.low()
            lRed.low()

    while True:
        timeHandler()
        # c.check_msg()
        check_rfid()