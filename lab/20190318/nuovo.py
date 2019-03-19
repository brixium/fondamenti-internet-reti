import requests
import matplotlib.pyplot as plt

plt.figure()
siti = ["http://www.polimi.it", "http://www.google.it", "http://www.netflix.com"]

for ID_url, url in enumerate(siti):
	print(ID_url+1, 'Test ', url)
	tempi = []
	for _ in range(5):
		r = requests.get(url)
		tempi.append(r.elapsed.microseconds/1000)
	plt.plot(tempi, label=url) # il valore in più mettiamo la label con stesso nome di url
	print("MIN: ", min(tempi), "\nMAX: ", max(tempi), "\nAVG: ", sum(tempi)/len(tempi))
# la funzione enumerate resituisce una lista con indice del vettore e il suo valore
plt.xlabel("ID richiesta")
plt.ylabel("[ms]")
plt.title("Test tempi di risposta")
plt.legend(loc='upper right', fontsize=15) # stampiamo la legenda in basso a dx 
plt.grid()
plt.show()
