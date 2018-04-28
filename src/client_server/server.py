import socket
from client_server.helper import load_staff_list

STAFF_FILENAME = "src/client_server/output/server_staff.xlsx"
ROOM_FILENAME = "src/client_server/output/server_room.xlsx"

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
while True:
    print("Waiting...")
    conn, addr = s.accept()
    print('Connected by', addr)

    # Save to file
    with open(STAFF_FILENAME, 'wb') as f:
        while True:
            print('receiving data...')
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    f.close()

    # Load staff list into a dataframe
    df = load_staff_list(STAFF_FILENAME)
    print(">>>>>>>>>>", df.columns)
    print(">>>>>>>>>>", df[df.columns[2]].head())

    conn.close()
