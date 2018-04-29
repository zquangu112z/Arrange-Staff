import socket
from client_server.helper import load_dataframe,\
    receive_1_file_ftp, arrange_staff, send_1_file_ftp
import pandas as pd

STAFF_FILENAME = "src/client_server/tmp/server_staff.xlsx"
ROOM_FILENAME = "src/client_server/tmp/server_room.xlsx"
RESULT_FILENAME = "src/client_server/tmp/result.xlsx"

host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    print("Waiting...")
    conn, addr = s.accept()
    print('Connected by', addr)

    # Save to file
    receive_1_file_ftp(STAFF_FILENAME, conn)
    receive_1_file_ftp(ROOM_FILENAME, conn)

    # Load staff list into a dataframe
    dfStaff = load_dataframe(STAFF_FILENAME)
    dfStaff = dfStaff[dfStaff.columns[1:5]]
    # print(dfStaff.head())
    '''
       Mã số  cán bộ                Họ Tên Trường  Ngày sinh
    0      106170001          Mai Chiếm An   ĐHBK        NaN
    1      106170002        Nguyễn Bảo Anh   ĐHBK        NaN
    2      106170003    Phan Thị Quỳnh Anh   ĐHBK        NaN
    3      106170004  Dương Văn Thanh Bình   ĐHBK        NaN
    4      106170005       Lương Hữu Chung   ĐHBK        NaN
    ...
    '''
    dfRoom = load_dataframe(ROOM_FILENAME)
    dfRoom = dfRoom[dfRoom.columns[1]]
    # print(dfRoom.head())
    '''
    0    C201
    1    C202
    2    C203
    3    C204
    4    C205
    ...
    '''
    dfStaff = arrange_staff(dfStaff, dfRoom)
    print(">>>>>>>>The result will be available at {}".format(RESULT_FILENAME))
    print("================")
    print(dfStaff[dfStaff.columns[1:5]].head())
    print("================")

    # Save result to ./tmp
    writer = pd.ExcelWriter(RESULT_FILENAME)
    dfStaff.to_excel(writer, 'Sheet1')
    writer.save()

    # Send result back to client
    send_1_file_ftp(RESULT_FILENAME, conn)

    conn.close()
