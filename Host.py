
import requests
import socket
import pickle


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#socket.SOCK_STREAM => whit TCP protocol
#socket.AF_INET => IPV4
local_host = '127.0.0.1'
local_port =808

'''
host_ip = socket.gethostbyname('www.quera.ir')
print(host_ip)
print(s.connect((host_ip, 80)))
'''

################# create host ################
print('start binding...')
s.bind((local_host, local_port))
print('start listening...')
s.listen()

print('waiting for connect...')
while True:
    new_socket, address = s.accept()
    print(type(new_socket))
    print(address)
    #new_socket.sendall(b'Hello my friend\n')
    a = ['hello','dear','welcome']
    data = pickle.dumps(a)
    print(type(data))
    print(data)
    new_socket.sendall(data)
    #new_socket.send(b'Hello my friend\n')
    for i in a:
        b = new_socket.recv(1024)
        print(b.decode())
        print('')
    a = new_socket.recv(1024)
    print(a)
    new_socket.close()

s.close()


