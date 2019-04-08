#trasporto con tcp
#trasferimento di bytes, connection-oriented
#nel server ci sono 2 socket: il welcome socket (per tutti per aprire conn.) e uno specifico con un client, connection socket
#il client specifica sempre IP addr e port number
#inputstream vs outputstream

#il client legge una riga dall'stdin e lo invia sulla socket
#sul client ci sono 2 coppie di in e 2 coppie di output
#netcat è un programmino che fa cose con server e clienta
# nc -t -l 1200
# netstat -tulp per vedere le connessioni attive
#in realtà la connessione dovrebbe durare finché il client non decide di smettere, cioè all'invio di un messaggio . e basta
#per gestire più client bisogna creare un workers per ciascun client. 2 casi:
	#1)ogni worker è un thread. Svantaggi: ha memoria condivisa con programma padre e max numero di thread paralleli. Vantaggi: facile e veloce
	#2)1 worker è un processo. Svantaggi: aggiunge complessità e latenza
#esiste anche un n.3: un solo worker che gestisce a turno un messaggio da ogni socket. Vantaggio di presatazioni, ma è difficile da gestire
