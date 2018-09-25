import socket

sockClient = socket.socket()
sockClient.connect(('127.0.0.1',7000))
sockClient.send("PING!!!!!!".encode())
dataDariServer = sockClient.recv(1024).decode()            
print ('dari server: ' + dataDariServer)
sockClient.close()