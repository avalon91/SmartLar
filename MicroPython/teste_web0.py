import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

f = open('teste.html')
html = f.read()

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl.send(html)
    cl.close()
