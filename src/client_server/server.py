import socket
from client_server.helper import load_staff_list, receive_file

STAFF_FILENAME = "src/client_server/output/server_staff.xlsx"
ROOM_FILENAME = "src/client_server/output/server_room.xlsx"

host = ''        # Symbolic name meaning all available interfaces
port = 12344     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
while True:
    print("Waiting...")
    conn, addr = s.accept()
    print('Connected by', addr)

    # Save to file
    receive_file(STAFF_FILENAME, conn)
    # receive_file(ROOM_FILENAME, conn)

    # Load staff list into a dataframe
    dfStaff = load_staff_list(STAFF_FILENAME)
    print(">>>>>>>>>>", dfStaff.columns)
    # print(">>>>>>>>>>", dfStaff[dfStaff.columns[1:3]].head())

    conn.close()
