import socket

STAFF_FILENAME = "data/Danh-sach-can-bo-coi-thi.xlsx"
ROOM_FILENAME = "data/Danh-sach-phong-thi.xlsx"

host = socket.gethostname()
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

with open(STAFF_FILENAME, "rb") as f:
    data = f.read(1024)
    while data:
        s.send(data)
        data = f.read(1024)
f.close()

# data = s.recv(1024)
s.close()
# print('Received', repr(data))
