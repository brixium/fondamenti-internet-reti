# esercizio diviso in due parti: A e B
import requests
medie = []
siti = ["http://www.polimi.it", "http://www.google.it", "http://www.netflix.com", "http://wikipedia.org", "http://www.gamebanana.com", "http://www.alexa.com"]
for ID_url, url in enumerate(siti):
	print(ID_url+1, 'Test ', url)
	tempi = []
	tentativi = 3
	for i in range(tentativi):
		r = requests.get(url)
		tempi.append(r.elapsed.microseconds/1000)
	part = 0
	for j in range(tentativi):
		part = part + tempi[j]
	medie.append(part)
	part = 0
	tempi = []
	if(ID_url % 2 == 1):
		print("Il più veloce tra", siti[ID_url-1], "e", siti[ID_url], "è")
		if(medie[ID_url-1]<medie[ID_url]):
			print(siti[ID_url-1], "con una velocità media di", medie[ID_url-1], "ms")
		else:
			print(siti[ID_url], "con una velocità media di", medie[ID_url], "ms")
