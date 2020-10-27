from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('127.0.0.1', 8899))

data = input("请输入您要发送的数据：")

client_socket.send(bytes(data, encoding="utf-8"))

recv = client_socket.recv(1024)

print("recv %s" % str(recv, encoding="utf-8"))

client_socket.close()
