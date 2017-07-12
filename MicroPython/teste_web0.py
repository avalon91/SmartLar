#def config():
import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

val1 = ''
val2 = ''

#f = open('teste.html')
#html = f.read()

html = """<!DOCTYPE html>
<html>
<head> <title>Teste</title> </head>
    <body> <h1>Funcionou!</h1> <br>
        <form>
            Campo 1:<br>
            <input type="text" name="campo1"><br>
            Campo 2:<br>
            <input type="text" name="campo2"><br>
            <input type="submit" value="Enviar">
        </form>
    </body>
<html>"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    conn, addr = s.accept()
    print('client connected from %s' % str(addr))
    request = conn.recv(1024)
    print('content = %s' % str(request))
    request = str(request)
    campo1 = request.find('campo1=')
    campo2 = request.find('campo2=')
    print(campo1)
    print(campo2)
    if(campo1 > 0 and campo1 < 50):
        str1 = ''
        cont = 0
        beg = campo1+7
        for i in request:
            if cont >= beg:
                if i != '&':
                    str1 = str1 + i
                if i == '&':
                    break
            cont = cont + 1
        val1 = str1
    if(campo2 > 0 and campo2 < 50):
        str2 = ''
        cont = 0
        beg = campo2+7
        for i in request:
            if cont >= beg:
                if i != '\\':
                    str2 = str2 + i
                if i == '\\':
                    break
            cont = cont + 1
        val2 = str2
    if val1 != '':
        print('val1: ' + val1)
    if val2 != '':
        print('val2: ' + val2)
    response = html
    conn.send(response)
    conn.close()
