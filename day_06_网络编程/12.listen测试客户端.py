from socket import *
import time

conn_num = int(input("请输入最大连接长度："))

for i in range(conn_num):
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(("127.0.0.1", 7788))
    tcp_socket.send(bytes("hello", encoding="utf-8"))
    print(i)
