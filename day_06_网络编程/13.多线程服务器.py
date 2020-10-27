from socket import *
from threading import Thread


def deal_with_client(new_socket, dest_addr):
    while True:
        rev_data = new_socket.recv(1024)
        if len(rev_data) > 0:
            print("recv[%s]:%s" % (str(dest_addr), str(rev_data, encoding="utf-8")))
        else:
            print("[%s]客户端已经关闭" % (str(dest_addr)))
            break
    new_socket.close()


def main():
    ser_socket = socket(AF_INET, SOCK_STREAM)
    ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    local_addr = ("", 7788)
    ser_socket.bind(local_addr)
    ser_socket.listen(5)

    try:
        while True:
            print("----主线程，等待新的客户端的到来----")
            new_socket, dest_addr = ser_socket.accept()

            print("----主线程，接下来交给一个线程处理数据[%s]----" % str(dest_addr))
            client = Thread(target=deal_with_client, args=(new_socket, dest_addr))
            client.start()
    finally:
        ser_socket.close()


if __name__ == '__main__':
    main()
