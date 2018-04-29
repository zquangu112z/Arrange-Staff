import socket
from client_server.helper import send_1_file_ftp

STAFF_FILENAME = "data/Danh-sach-can-bo-coi-thi.xlsx"
ROOM_FILENAME = "data/Danh-sach-phong-thi.xlsx"

host = socket.gethostname()
port = 12344                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Send the first file
send_1_file_ftp(STAFF_FILENAME, s)
send_1_file_ftp(ROOM_FILENAME, s)

s.close()
