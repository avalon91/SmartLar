tp2 = 0

def conectar():
    import mfrc522, time, json, utime, urequests
    from os import uname
    from machine import Pin

    lGre = Pin(13, Pin.OUT)
    lRed = Pin(12, Pin.OUT)
    rele = Pin(16, Pin.OUT)
    rele.off()

    linkEntrada = 'http://lar.ect.ufrn.br:8080/api/v1/verificar-entrada/'

    rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

    def check_rfid():
        uid = ""
        global tp2
        (stat, tag_type) = rdr.request(rdr.REQIDL)

        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                for i in range(0, 4):
                    uid = uid + "%02x" % raw_uid[i]
                uid = uid.upper()
                print(uid)
                if uid == '647A19B8' or uid == 'E696D04B' or uid == '72D0D54B' or uid == '2D30CE4B' or uid == '1DAFDF4B' or uid == 'E617D247':
                    linkCompl = linkEntrada + uid
                    rele.on()
                    tp2 = utime.ticks_ms()
                    perm = json.loads(urequests.get(linkCompl).content)
                    print('Ola')
                    if perm:
                        print('Conectado e verificado')
                else:
                    linkCompl = linkEntrada + uid
                    perm = json.loads(urequests.get(linkCompl).content)
                    if perm == True:
                        rele.on()
                        tp2 = utime.ticks_ms()
                        print('Entrada permitida')
                    elif perm == False:
                        lRed.on()
                        tp2 = utime.ticks_ms()
                        print('Entrada negada')
                # uid = uid + "0"
                # c.publish(TOPIC1, b"%s" % uid)
                lGre.on()
    
    def timeHandler():
        if((rele.value() == True) and (utime.ticks_diff(utime.ticks_ms(), tp2) >= 5000)):
            lGre.off()
            rele.off()
            print('Fechou')
        elif((lRed.value() == True) and (utime.ticks_diff(utime.ticks_ms(), tp2) >= 2000)):
            lGre.off()
            lRed.off()

    while True:
        timeHandler()
        # c.check_msg()
        check_rfid()