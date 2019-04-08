#server tcp
from socket import *

serverPort = 12000
#SOCK_STREAM e non più SOCK_DGRAM
serverSocket = socket(AF_INET, SOCK_STREAM)
#tupla con da chi attendi connessione come 1mo paramentro '' significa tutti, e poi la porta
serverSocket.bind(('', serverPort)) #welcome socket
#questo fa sempre parte del welcome socket, attende connessioni
serverSocket.listen(1) # 1 è la dimensione della coda di connessioni incomplete (in questo caso 1 vuol dire che la coda di backlog è 1+valore specificato (su linux, su win è solo 1))
print('Il server è pronto')
while True:
	#accept con due parametri: CONNECTION_SOCKET e INDIRIZZO_CLIENT
	connectionSocket, clientAddress = serverSocket.accept() #active open
	print('Sono connesso con un client')
	#modifica 1: ciclo interno made by me (queste 2 righe)
	while True:
		messaggio = connectionSocket.recv(1024)
		messaggio = messaggio.decode('utf-8')
		#modifica 2 fatta dal profe
		if messaggio == '.':
			break
		messaggio = messaggio.upper()
		connectionSocket.send(messaggio.encode('utf-8'))

	connectionSocket.close()

#come modifichiamo questo server?
#adesso facciamo il server multithread
