from socket import *

import select
import sys

ser_socket = socket(AF_INET, SOCK_STREAM)
local_addr = ("", 7788)
ser_socket.bind(local_addr)
# 变为非阻塞
ser_socket.listen(5)

inputs = [ser_socket]

running = True

while running:
    readable, writeable, exceptional = select.select(inputs, [], [])

    for sock in readable:
        if sock == ser_socket:
            conn, addr = ser_socket.accept()

            inputs.append(conn)
        # 键盘输入
        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break
        # 数据到达
        else:
            data = sock.recv(1024)
            if data:
                sock.send(data)
            else:
                # 移除select 监听
                inputs.remove(sock)
                sock.close()