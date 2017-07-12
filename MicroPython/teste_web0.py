#def config():
import socket, json
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

val1 = ''
val2 = ''
val3 = ''
val4 = ''
val5 = ''

preJson = open('config.txt').read()
data = json.loads(preJson)
config = data['campos']

html = open('teste.html').read()
# f = open('teste.html')
# html = f.read()
# f.close()

# html = """<!DOCTYPE html>
# <html>
# <head> <title>Teste</title> </head>
#     <body> <h1>Funcionou!</h1> <br>
#         <form>
#             Campo 1:<br>
#             <input type="text" name="campo1"><br>
#             Campo 2:<br>
#             <input type="text" name="campo2"><br>
#             <input type="submit" value="Enviar">
#         </form>
#     </body>
# <html>"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    conn, addr = s.accept()
    print('client connected from %s' % str(addr))
    request = conn.recv(1024)
    # print('content = %s' % str(request))
    request = str(request)
    ssid = request.find('ssid=')
    senha = request.find('senha=')
    ip = request.find('ip=')
    paswd = request.find('paswd=')
    porta = request.find('porta=')
    # print(ssid)
    # print(porta)
    if(ssid > 0 and ssid < 50):
        str1 = ''
        cont = 0
        beg = ssid+5
        for i in request:
            if cont >= beg:
                if i != '&':
                    str1 = str1 + i
                if i == '&':
                    break
            cont = cont + 1
        val1 = str1
    if(senha > 0 and senha < 50):
        str2 = ''
        cont = 0
        beg = senha+6
        for i in request:
            if cont >= beg:
                if i != '&':
                    str2 = str2 + i
                if i == '&':
                    break
            cont = cont + 1
        val2 = str2
    if(ip > 0 and ip < 50):
        str3 = ''
        cont = 0
        beg = ip+3
        for i in request:
            if cont >= beg:
                if i != '&':
                    str3 = str3 + i
                if i == '&':
                    break
            cont = cont + 1
        val3 = str3
    if(paswd > 0 and paswd < 60):
        str4 = ''
        cont = 0
        beg = paswd+6
        for i in request:
            if cont >= beg:
                if i != '&':
                    str4 = str4 + i
                if i == '&':
                    break
            cont = cont + 1
        val4 = str4
    if(porta > 0 and porta < 70):
        str5 = ''
        cont = 0
        beg = porta+6
        for i in request:
            if cont >= beg:
                if i != '\\' and i != ' ':
                    str5 = str5 + i
                if i == '\\' or i == ' ':
                    break
            cont = cont + 1
        val5 = str5
    if val1 != '':
        print('val1: ' + val1)
        config[0] = val1
    if val2 != '':
        print('val2: ' + val2)
        config[1] = val2
    if val3 != '':
        print('val3: ' + val3)
        config[2] = val3
    if val4 != '':
        print('val4: ' + val4)
        config[3] = val4
    if val5 != '':
        print('val5: ' + val5)
        config[4] = val5
    data['campos'] = config
    dataIn = json.dumps(data)
    f = open('config.txt', 'w')
    f.write(dataIn)
    f.close()
    response = html
    conn.send(response)
    conn.close()
