import socket
import os
from client_server.helper import send_file_ftp


s = socket.socket()
host = socket.gethostname()
port = 9001
s.connect((host, port))
path = "data/"
directory = os.listdir(path)


for file in directory:
    send_file_ftp(path, file, s)

s.close()
