import socket

dest = ("<broadcast>", 7788)

# 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 对需要发送广播的套接字进行修改，否则不能发送广播
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# 以广播的形式发送到本网络所有电脑
s.sendto(bytes("Hi", encoding="utf-8"), dest)

print("等待对方回复")

while True:
    (buf, address) = s.recvfrom(2048)
    print("received from %s:%s" % (address, str(buf, encoding="utf-8")))
