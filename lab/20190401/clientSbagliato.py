from socket import *

serverName = "127.0.0.1"
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Mani in alto, dammi i soldi! ")

clientSocket.sendto(message.encode('utf8'), (serverName, serverPort))
clientSocket.close()

# non cambia niente perché è UDP (non affidabile)
