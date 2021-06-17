import requests
import os
import random
import string
import json

# Definição de caracteres usados para gerar uma senha randomica
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# Inserir nesta variável a url do formulário que deseja floodar
url = ''

# Lendo a lista dos 1000 nomes mais comuns da língua inglesa
names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
        # Inserir o username e password pegos no Form Data
	    '': username,
		'': password
	})

	print ("Enviando usuário: " + username + "e senha: " + password + "para o endereço:" + url)