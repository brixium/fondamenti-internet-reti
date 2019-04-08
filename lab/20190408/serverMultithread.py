#server tcp
from socket import *
from threading import *

def handler(connectionSocket):
	while True:
		messaggio = connectionSocket.recv(1024)
		if messaggio.decode('utf-8') == '.':
			break
		messaggioMaiusc = messaggio.decode('utf-8').upper()
		connectionSocket.send(messaggioMaiusc.encode('utf-8'))
	connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

#permette al socket locale di usare la stessa porta su diversi connectionsocket contemporaneamente
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('', serverPort)) #welcome socket
serverSocket.listen(1)

while True:
	newSocket, addr = serverSocket.accept()
	#avviamo il thread
	thread = Thread(target=handler, args = (newSocket, ))
	thread.start() # non è bloccante questa istruzione, a differenza della accept
