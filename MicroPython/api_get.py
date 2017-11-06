import json, urequests

# response = urequests.get('http://lar.ect.ufrn.br:8080/api/v1/user/2013023070') #matricula
# response = urequests.get('http://lar.ect.ufrn.br:8080/api/v1/user/3EB89F2C') #rfid
# usuario = json.loads(response.content)
# response.close()

usuario = json.loads(urequests.get('http://lar.ect.ufrn.br:8080/api/v1/user/20170184418').content)

print usuario['nome']

perm = json.loads(urequests.get('http://lar.ect.ufrn.br:8080/api/v1/verificar-entrada/951C51AC').content)
if perm == True:
    print 'Pode entrar'
else:
    print 'Não pode entrar'
