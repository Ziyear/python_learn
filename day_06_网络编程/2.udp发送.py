from socket import *

# 1创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)
# 2准备发送地址
sendAdd = ('127.0.0.1', 8080)
# 3获取发送内容
while True:
    sendData = input("请输入你要发送的内容：")
    # 4发送
    udpSocket.sendto(bytes(sendData, encoding='utf8'), sendAdd)
    if sendData == 'Bye':
        break
# 5关闭
udpSocket.close()
