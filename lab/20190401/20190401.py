#oggi lezione con socket UDP
#solo python versione 3 e pycharm, garantita interoperabilità
#obiettivo: sviluppare applicazioni lient server con il socket
#Socket API introdotto in BSD4.1 nel 1981. 2 tipi di servizio: UDP e TCP. Si possono inviare messaggi (UDP) o stream di dati (TCP).
#server già in esecuzione (deamon) con una porta aperta. Anche il client deve avere una porta attiva. Il client deve conoscere a priori IP e porta del server
#UDP è connectionless e best effort. Gestire a livello applicativo gli errori
#in questa applicazione il client scrive una riga di testo e la invia al server che la restituisce tutta maiuscola
#prima cosa sul server è creare il socket.
#alla fine del programma udp client devi chiudere il socket
#utente inserisce dalla tastiera e invia la stringa dal clientSocket al server

#client e server utilizzano entrambi datagramSocket
# per vedere i socket aperti da linux devi usare netstat con parametro -tult
#Modifica #1
#Modificare il server per stampare indirizzo IP e porta del client che ha effettuato la richiesta
#Modifica #2
#Gestire le eccezioni e impostare un timeout con il metodo settimeout()
#per gestire le eccezioni i blocchi sono try, except e finally, seguiti da : e indentare correttamente le istruzioni


