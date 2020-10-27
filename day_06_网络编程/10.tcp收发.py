from socket import *

if __name__ == '__main__':
    client_socket = socket(AF_INET, SOCK_STREAM)

    client_socket.connect(('127.0.0.1', 7788))

    while True:
        data = input("请输入您要发送的数据：")
        client_socket.send(bytes(data, encoding="utf-8"))
        recv = client_socket.recv(1024)
        print("接收到的数据 %s" % str(recv, encoding="utf-8"))
        if len(data) <= 0:
            break

    client_socket.close()
