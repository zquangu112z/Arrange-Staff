import socket
from client_server.helper import send_1_file_ftp, receive_1_file_ftp

STAFF_FILENAME = "data/Danh-sach-can-bo-coi-thi.xlsx"
ROOM_FILENAME = "data/Danh-sach-phong-thi.xlsx"
RESULT_FILENAME = "src/client_server/output/result.xlsx"

host = socket.gethostname()
port = 12354
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Send the first file
send_1_file_ftp(STAFF_FILENAME, s)
send_1_file_ftp(ROOM_FILENAME, s)

# Save the result received from server
receive_1_file_ftp(RESULT_FILENAME, s)
s.close()
