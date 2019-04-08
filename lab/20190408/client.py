#client tcp
from socket import *

serverName = '127.0.0.1'
serverPort = 12000
#socket del client
clientSocket = socket(AF_INET, SOCK_STREAM)
#connessione con parametro una tupla di 2 elementi
clientSocket.connect((serverName, serverPort))

#modifica 1: while true per ciclo infinito
while True:
	messaggio = input("Inserisci una frase (con un . termini la connessione): ")
	messaggio = messaggio.encode('utf-8')
	#sentTo era per UDP, con TCP abbiamo aperto una connessione in precedenza
	clientSocket.send(messaggio)

	#modifica 2: questa per terminare subito dopo il punto
	if messaggio.decode('utf-8') == '.':
		break
	
	#contrariamente ad UDP che aveva la receiveFrom, qui abbiamo la receive, che vuole in ingresso la q.ta del buffer
	messaggioModificato = clientSocket.recv(1024)
	print(messaggioModificato.decode('utf-8'))

clientSocket.close()
