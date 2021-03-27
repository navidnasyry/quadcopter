from socket import *

IPaddress = '127.0.0.1'
Port = 120

socketServer = socket(AF_INET, SOCK_STREAM)
socketServer.bind((IPaddress, Port))
socketServer.listen(5)
print('The server is ready to receive...')
while True:
    connectionSocket, addr = socketServer.accept()
    sentence = connectionSocket.recv(1024).decode().upper()
    print('recived from ')
    for i in addr:
        print(i)
    connectionSocket.send(sentence.encode())
    connectionSocket.close()


