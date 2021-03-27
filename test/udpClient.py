from socket import *

serverName = "127.0.0.1" # IP address of the server or its hostname
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
#SOCK_DGRAM => UDP
#AF_INET => using IPv4
message = input('input lowercase sentence : ')
clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('From UDP Server : ', modifiedMessage.decode())
clientSocket.close()



