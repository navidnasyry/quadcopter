import socket
import pickle


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 808

print('connecting to host...')
s.connect((host,port))

# = s.recv(1024)
receve_data = s.recv(1024)
receved_list= pickle.loads(receve_data)
print(type(receved_list))
for i in receved_list:
    print(i)
    c = i.upper()
    s.send(c.encode())

#b_2 = b.decode('utf-8')
s.sendall(b'now Iam Client...and send message to you.')
#s.sendall(['salam','khoobi'])
#print(b_2)
#print(type(b_2))
#print(str(b))
#print(type(b))
s.close()