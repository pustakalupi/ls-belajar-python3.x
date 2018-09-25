import socket

sockServer = socket.socket()
sockServer.bind(("127.0.0.1",7000))

sockServer.listen(1)
sockClient, address = sockServer.accept()
print ("ada koneksi dari: " + str(address))

while True:
        data = sockClient.recv(1024).decode()
        if not data:
                break
        print ("data dari client: " + str(data))
        print ("kirim balik: " + str(data))
        sockClient.send(data.encode())

sockClient.close()