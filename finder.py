import re
import requests 
from googlesearch import search

txt = input('Interesse: ')
nsite = int(input('Qnt: '))
c = 0

print('Starting E-mail Finder...\n') 
for url in search(txt):
	try:
		req = requests.get(url)
	except Exception as erro:
		print(str(erro)+'\n')

	email = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req.text)
	if email:
		c+=1
		print('URL: ' + url)
		print('E-MAIL: ' + str(email) + '\n')
		if c == nsite:
			break
