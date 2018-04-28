import socket

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
    with open('server_log.xlsx', 'wb') as f:
        while True:
            print('receiving data...')
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    f.close()
    conn.close()
