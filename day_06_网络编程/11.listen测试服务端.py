from socket import *
import time

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(("", 7788))

conn_num = int(input("请输入最大连接长度："))

tcp_socket.listen(conn_num)
for i in range(10):
    print(i)
    time.sleep(1)
print("延时结束")
while True:
    new_socket, client_addr = tcp_socket.accept()
    print(client_addr)
    time.sleep(1)
