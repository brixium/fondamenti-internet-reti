#partiamo dal client udp

#importiamo tutti i moduli della libreria socket
from socket import * 

#impostiamo il nome del server (in questo caso il localhost) e la porta
serverName = "127.0.0.1"
serverPort = 1200

#creiamo il socket. Primo parametro è versione del protocollo ip (il nostro è 4)
#secondo parametro è definire se UDP o TCP 
clientSocket = socket(AF_INET, SOCK_DGRAM)
#facciamo inserire dal client il testo
message = input("Inserisci il messaggio: ")

#modifica 2: gestisco l'eccezione con i blocchi try, except e finally
try:
	#invio messaggio
	clientSocket.sendto(message.encode('utf8'), (serverName, serverPort))
		#primo parametro è il messaggio codificato con UTF-8
		#secondo è una tupla contente: indirizzo del server,porta
	
	#modifica 2: impostiamo un timeout (di n secondi) sulla connessione in uscita
	clientSocket.settimeout(2)
	
	#riceviamo il messaggio in uscita dal server. Il metodo restituisce queste due cose
	messaggioModificato, serverAddress = clientSocket.recvfrom(2048)
		#parametro della receive è la lunghezza del buffer
	#decodifichiamo da utf-8
	messaggioModificato = messaggioModificato.decode('utf-8')
	print("Messaggio modificato: ", messaggioModificato)
	#chiudiamo il socket in ascolto sulla porta
except:
	print("C'è stato un erroraccio e ora morirai")
finally:
	clientSocket.close()
