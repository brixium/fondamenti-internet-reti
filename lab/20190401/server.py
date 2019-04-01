#server
from socket import *

#definire la porta di ascolto
serverPort = 1200
#creazione del server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
#apertura del ss (con bind)
serverSocket.bind(('', serverPort))
	#parametro: tupla con indirizzo in ascolto e porta in ascolto (siccome non siamo in ascolto di messaggi da un particolare IP lasciamo vuoto)
#print('Server pronto a ricevere')
#ciclo infinito per il server
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
		#2048 è dimensione buffer
		#recvfrom restituisce messaggio e indirizzo del client
	message = message.decode('utf-8')
	print("Ricevuto", message, "da", clientAddress[0], "sulla porta", clientAddress[1])
	#mette tutta la stringa in maiuscolo
	modifiedMessage = message.upper()
	#inviare a <parametri>
	serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
		#1mo par. è il messaggio codificato, 2ndo è indirizzo a cui spedire
	
