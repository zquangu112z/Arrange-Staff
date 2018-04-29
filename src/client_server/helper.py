import pandas as pd


def load_staff_list(filename):
    dfs = pd.read_excel(filename, sheet_name='Sheet1')
    df = pd.DataFrame(dfs, columns=dfs.keys())
    return df


def send_file(filename, socket):
    with open(filename, "rb") as f:
        for data in f:
            socket.sendall(data)
    f.close()
    print(">>>>>Sent {}".format(filename))


def receive_file(filename, socket):
    with open(filename, 'wb') as f:
        while True:
            print('receiving data...')
            data = socket.recv(1024)
            if not data:
                print(">>>>>>>>>>>Not data")
                break
            f.write(data)
    f.close()
    print("Saved file")
