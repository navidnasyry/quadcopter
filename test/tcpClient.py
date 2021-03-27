from socket import *


serverName = '127.0.0.1'
portName = 120
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, portName))
sentence = input('input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From TCP Server : ', modifiedSentence.decode())
clientSocket.close()