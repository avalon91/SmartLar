#https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
#https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_pub.py
#https://github.com/micropython/micropython-lib/pull/91#issuecomment-239030008

def conectar():
    import mfrc522, machine, time, network, json
    from os import uname
    from umqtt.simple import MQTTClient

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
    TOPIC = b"/rfid/normal"
    ID = "esp"
    USER = config[4].encode()
    PASSWORD = config[3].encode()

    c = MQTTClient(ID, SERVER, user=USER, password=PASSWORD)
    c.connect()


    while True:
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
                c.publish(TOPIC, b"%s" % uid)
                #c.disconnect()
