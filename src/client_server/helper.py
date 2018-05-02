import pandas as pd
import os


def load_dataframe(filename):
    dfs = pd.read_excel(filename, sheet_name='Sheet1')
    df = pd.DataFrame(dfs, columns=dfs.keys())
    return df


def arrange_staff(dfStaff, dfRoom):
    # shuffle the list of staff
    dfStaff = dfStaff.sample(frac=1)
    if(len(dfRoom) > 2 * len(dfStaff)):
        print("There is not enough staff. Please add more staff.")
        return None

    len_room = len(dfRoom)

    # GIÁM THỊ 1
    dfRoom.insert(
        loc=len(dfRoom.iloc[0]),
        column="Giám thị 1",
        value=dfStaff[dfStaff.columns[1]][0:len_room].values)

    dfRoom.insert(
        loc=len(dfRoom.iloc[0]),
        column="Mã số giám thị 1",
        value=dfStaff[dfStaff.columns[0]][:len_room].values)

    # GIÁM THỊ 2
    dfRoom.insert(
        loc=len(dfRoom.iloc[0]),
        column="Giám thị 2",
        value=dfStaff[dfStaff.columns[1]][len_room:2 * len_room].values)

    dfRoom.insert(
        loc=len(dfRoom.iloc[0]),
        column="Mã số giám thị 2",
        value=dfStaff[dfStaff.columns[0]][len_room:2 * len_room].values)

    # GIÁM THỊ HÀNH LANG @TODO: optimize the code
    nonAssignedStaff = dfStaff[dfStaff.columns[1]][2 * len(dfRoom):].values
    nonAssignedStaffCode = dfStaff[dfStaff.columns[0]][2 * len(dfRoom):].values

    num_lobby = int(len_room / len(nonAssignedStaff))
    dfStaffLobby = []
    dfStaffLobbyCode = []
    for i in range(len(nonAssignedStaff) - 1):
        for j in range(num_lobby):
            dfStaffLobby.append(nonAssignedStaff[i])
            dfStaffLobbyCode.append(nonAssignedStaffCode[i])

    for i in range(num_lobby * (len(nonAssignedStaff) - 1), len_room):
        dfStaffLobby.append(nonAssignedStaff[len(nonAssignedStaff) - 1])
        dfStaffLobbyCode.append(
            nonAssignedStaffCode[len(nonAssignedStaffCode) - 1])

    dfRoom.insert(
        loc=len(dfRoom.iloc[0]),
        column="Giám thị hành lang",
        value=dfStaffLobby)

    dfRoom.insert(
        loc=len(dfRoom.iloc[0]),
        column="Mã số giá thị hành lang",
        value=dfStaffLobbyCode)

    return dfRoom


def send_1_file_ftp(filename, socket):
    filesize = os.path.getsize(filename)
    # encode filesize as 32 bit binary
    filesize = str(filesize).encode('utf-8').zfill(32)
    socket.send(filesize)

    fileToSend = open(filename, 'rb')

    socket.sendall(fileToSend.read())
    fileToSend.close()
    print('File Sent')


def receive_1_file_ftp(filename, socket):
    filesize = socket.recv(32)
    filesize = int(filesize)
    file_to_write = open(filename, 'wb')
    chunksize = 4096
    while filesize > 0:
        if filesize < chunksize:
            chunksize = filesize
        data = socket.recv(chunksize)
        file_to_write.write(data)
        filesize -= len(data)

    file_to_write.close()
    print('File received successfully')


def send_file_ftp(path, file, socket):
    print(file)
    filename = file.encode('utf-8')
    size = len(filename)
    # encode filename size as 16 bit binary
    size = str(size).encode('utf-8').zfill(16)
    print(size)
    socket.send(size)
    socket.send(filename)

    filename = os.path.join(path, file)
    filesize = os.path.getsize(filename)
    # encode filesize as 32 bit binary
    filesize = str(filesize).encode('utf-8').zfill(32)
    socket.send(filesize)

    fileToSend = open(filename, 'rb')

    socket.sendall(fileToSend.read())
    fileToSend.close()
    print('File Sent')


def receive_file_ftp(socket):
    while True:
        # Note that you limit your filename length to 255 bytes.
        size = socket.recv(16)
        if not size:
            break
        size = int(size)
        print(size)
        filename = socket.recv(size).decode('utf-8')
        print(filename)
        filesize = socket.recv(32)
        filesize = int(filesize)
        file_to_write = open(filename, 'wb')
        chunksize = 4096
        while filesize > 0:
            if filesize < chunksize:
                chunksize = filesize
            data = socket.recv(chunksize)
            file_to_write.write(data)
            filesize -= len(data)

        file_to_write.close()
        print('File received successfully')


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
