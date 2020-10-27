from socket import *

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 2. 绑定一个本地信息
local_addr = ("127.0.0.1", 8080)
udp_socket.bind(local_addr)
# 3. 接收数据
while True:
    recv_data = udp_socket.recvfrom(1024)
    data_ = recv_data[0]
    recv_msg = str(data_, encoding="utf-8")
    send_addr = recv_data[1]
    # 在发送给发送方
    udp_socket.sendto(data_, send_addr)
    # 4. 打印接收到的信息
    print("%s:%s" % (str(send_addr), recv_msg))
    if recv_msg == 'Bye':
        break
# 5. 关闭套接字
udp_socket.close()
