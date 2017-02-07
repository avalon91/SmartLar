def conectar():
    import network
    import time
    flag = False
    count = 0
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect('Rockbox Z', 'sacidepatinete')
        print('Conectando na rede Rockbox Z...')
        #wlan.connect('BonoNet', 'bonooliveira402')
        #print('Conectando na rede BonoNet...')
        for i in range(0, 9):
            if wlan.isconnected():
                flag = True
                count = 0
                break
            count = count + 1
            time.sleep(1)
        if count == 9:
            count = 0
            wlan.connect('BonoNet', 'bonooliveira402')
            print('Conectando na rede BonoNet...')
            #wlan.connect('LAR-ECT', 'senhafacil1234')
            #print('Conectando na rede LAR-ECT...')
            for i in range(0, 9):
                if wlan.isconnected():
                    flag = True
                    count = 0
                    break
                count = count + 1
                time.sleep(1)
        if count == 9:
            count = 0
            wlan.connect('LAR-ECT', 'senhafacil1234')
            print('Conectando na rede LAR-ECT...')
            #wlan.connect('Rockbox Turbo', 'sacidepatinete')
            #print('Conectando na rede Rockbox Turbo...')
            for i in range(0, 9):
                if wlan.isconnected():
                    flag = True
                    break
                time.sleep(1)
    if flag == True:
        print('Conectado')
        print(wlan.ifconfig())
        return True
    elif wlan.isconnected():
        print('Conectado')
        print(wlan.ifconfig())
        return True
    elif flag == False:
        print('Conexao falhou')
        return False
        #while not wlan.isconnected():
            #pass
