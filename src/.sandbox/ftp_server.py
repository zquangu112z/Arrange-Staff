import socket
from client_server.helper import receive_file_ftp

serversock = socket.socket()
host = socket.gethostname()
port = 9001
serversock.bind((host, port))
filename = ""
serversock.listen(10)
print("Waiting for a connection.....")

clientsocket, addr = serversock.accept()
print("Got a connection from %s" % str(addr))
receive_file_ftp(clientsocket)
serversock.close()
