import pandas as pd


def load_staff_list(filename):
    dfs = pd.read_excel(filename, sheet_name='Sheet1')
    df = pd.DataFrame(dfs, columns=dfs.keys())
    return df


def send_file(filename, socket):
    with open(filename, "rb") as f:
        data = f.read(1024)
        while data:
            socket.send(data)
            data = f.read(1024)
    f.close()
    socket.send(b"ENDED")
    print(">>>>>Sent {}".format(filename))


def receive_file(filename, socket):
    with open(filename, 'wb') as f:
        while True:
            print('receiving data...')
            data = socket.recv(1024)
            if not data:
                break
                continue
            if data == b'ENDED':
                break
            f.write(data)
    f.close()
