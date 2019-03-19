# esercizio diviso in due parti: A e B
import requests
medie = []
siti = ["http://www.polimi.it", "http://www.google.it", "http://www.netflix.com", "http://wikipedia.org", "http://www.gamebanana.com", "http://www.alexa.com"]
for ID_url, url in enumerate(siti):
	print(ID_url+1, 'Test ', url)
	tempi = []
	for _ in range(1):
		r = requests.get(url)
		tempi.append(r.elapsed.microseconds/1000)
		average = sum(tempi)/len(tempi)
		#print("AVG: ", average)
	medie.append(average)
	if(ID_url > 1 and ID_url % 2 == 0):
		print(siti[ID_url-1]," VS",siti[ID_url], "vince ") #soluzione di merda
		if(medie[-1] < medie[-2]):
			print(siti[ID_url-1])
		else:
			print(siti[ID_url])

