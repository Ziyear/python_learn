from socket import *

if __name__ == '__main__':
    client_socket = socket(AF_INET, SOCK_STREAM)
    port = int(input("请输入端口号："))
    client_socket.connect(('127.0.0.1', port))

    while True:
        data = input("请输入您要发送的数据：")
        if data == "" or data == "quit" or data == "exit":
            print("bye")
            break
        client_socket.send(bytes(data, encoding="utf-8"))
        recv = client_socket.recv(1024)
        print("接收到的数据 %s" % str(recv, encoding="utf-8"))

    client_socket.close()
