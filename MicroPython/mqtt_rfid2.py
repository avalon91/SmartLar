#https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
#https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_pub.py
#https://github.com/micropython/micropython-lib/pull/91#issuecomment-239030008

tp2 = 0

def conectar():
    import mfrc522, machine, time, network, json, utime
    from os import uname
    from umqtt.simple import MQTTClient

    lGre = machine.Pin(13, machine.Pin.OUT)
    lRed = machine.Pin(12, machine.Pin.OUT)

    if uname()[0] == 'WiPy':
        rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")

    elif uname()[0] == 'esp8266':
        rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

    else:
        raise RuntimeError("Unsupported platform")

    preJson = open('config.txt').read()
    data = json.loads(preJson)
    config = data['campos']

    SERVER = config[2]
    TOPIC1 = b"/rfid/normal"
    TOPIC2 = b"/rfid/teste"
    ID = "esp"
    USER = config[4].encode()
    PASSWORD = config[3].encode()

    def sub_cb(topic, msg):
        #print((topic, msg))
        global tp2
        msg = msg.decode("utf-8")
        print(msg)
        if msg == '1':
            lGre.high()
            tp2 = utime.ticks_ms()
        if msg == '0':
            lRed.high()
            tp2 = utime.ticks_ms()

    c = MQTTClient(ID, SERVER, user=USER, password=PASSWORD)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC2)

    def check_rfid():
        uid = ""

        # print("")
        # print("Place card before reader to read from address 0x08")
        # print("")

        (stat, tag_type) = rdr.request(rdr.REQIDL)

        if stat == rdr.OK:

            (stat, raw_uid) = rdr.anticoll()

            if stat == rdr.OK:

                #print("New card detected")
                #print("  - tag type: 0x%02x" % tag_type)
                #print("%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))

                for i in range(0, 4):
                    uid = uid + "%02x" % raw_uid[i]
                uid = uid + "0"
                #c.connect()
                c.publish(TOPIC1, b"%s" % uid)
                #c.disconnect()

    def timeHandler():
        if((lGre.value() == True) and (utime.ticks_diff(utime.ticks_ms(), tp2) >= 5000)):
            print(utime.ticks_diff(utime.ticks_ms(), tp2))
            lGre.low()
        # elif(flag == True):
        #     time2 = utime.ticks_ms()
        #     flag = None
        elif((lRed.value() == True) and (utime.ticks_diff(utime.ticks_ms(), tp2) >= 2000)):
            print(utime.ticks_diff(utime.ticks_ms(), tp2))
            lRed.low()
        # elif(flag == False):
        #     time2 = utime.ticks_ms()
        #     flag = None

    while True:
        check_rfid()
        c.check_msg()
        timeHandler()
        
        # uid = ""

        # # print("")
        # # print("Place card before reader to read from address 0x08")
        # # print("")

        # (stat, tag_type) = rdr.request(rdr.REQIDL)

        # if stat == rdr.OK:

        #     (stat, raw_uid) = rdr.anticoll()

        #     if stat == rdr.OK:

        #         #print("New card detected")
        #         #print("  - tag type: 0x%02x" % tag_type)
        #         #print("%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))

        #         for i in range(0, 4):
        #             uid = uid + "%02x" % raw_uid[i]
        #         uid = uid + "0"
        #         #c.connect()
        #         c.publish(TOPIC, b"%s" % uid)
        #         #c.disconnect()
        #         c.check_msg()
