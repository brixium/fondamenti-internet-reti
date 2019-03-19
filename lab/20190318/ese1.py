#visualizzare tempi di risposta di google. Usiamo il modulo requests ( http://docs.python-requests.org/en/master )
import requests
import matplotlib.pyplot as plt# per la rappresentazione grafica a partire da riga 34, lo shortcut sarà plt
# parametri: url, altri parametri
# (CTRL+Q dà la documentazione)
# r = requests.get("http://www.google.com")
# print(r.status_code)
# print(r.elapsed.microseconds/1000, "ms")  #restituisce il tempo espresso in millisecondi
# print("Tempo di risposta: " + str(r.elapsed.microseconds/1000) + " ms")  # si può fare anche così

# ora facciamolo 10 voltea

#for i in range(10): # al posto dell'indice del ciclo che non ci interessa usiamo un underscore
#	r = requests.get("http://www.google.com")
#	if r.status_code == 200:
#		print(str(i+1)+" Tempo di risposta: ", r.elapsed.microseconds/1000, " ms")  

# calcolare il minimo, medio e massimo delle 10 misurazioni
# la media aritmetica è mean() from statistics import mean
ris = []
avg = 0
for i in range(4):
	r = requests.get("http://www.google.com")
	if r.status_code == 200:
		ris.append(float(r.elapsed.microseconds/1000))
		avg = float(r.elapsed.microseconds/1000) + avg
avg = avg / 5

# oppure
avg = sum(ris) / len(ris)
# print(str(ris))
print("Min: ", min(ris),"\nMax: ", max(ris), "\nAvg: ", avg)

# stampare in forma grafica il risultato con matplotlib
# aprire la figura, inserire dentro i dati e poi stampare

plt.figure() # aprire figura
#plot del risultato
plt.plot(ris) #inseriamo i punti nel grafico
#decoraimo il grafico
plt.ylim([0, 1.1*max(ris)])
#visualizziamo
# plt.show()

#decoriamo ulteriormente con label sugli assi (moltiplicatore 1.1 sull'asse y)
plt.xlabel("ID richiesta")
plt.ylabel('[ms]')
plt.title("Test verso google.com")
plt.grid() # griglia

plt.show()

