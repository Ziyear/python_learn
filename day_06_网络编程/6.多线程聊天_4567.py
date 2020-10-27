from threading import Thread
from socket import *


# 收数据
def recvData():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        data_ = recv_data[0]
        recv_msg = str(data_, encoding="utf-8")
        send_addr = recv_data[1]
        print("\r >> %s:%s" % (send_addr, recv_msg), end="")


# 检测键盘，发送数据
def sendData():
    while True:
        sendInfo = input("<<")
        udp_socket.sendto(bytes(sendInfo, encoding='utf8'), ("127.0.0.1", 4568))


if __name__ == '__main__':
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 4567))

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)
    tr.start()
    ts.start()
    tr.join()
    ts.join()
