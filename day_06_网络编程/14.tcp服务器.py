from socket import *

# 单线程非阻塞
ser_socket = socket(AF_INET, SOCK_STREAM)
ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
local_addr = ("", 7788)
ser_socket.bind(local_addr)
# 变为非阻塞
ser_socket.setblocking(False)
ser_socket.listen(5)

client_list = []
while True:
    try:
        new_socket, dest_addr = ser_socket.accept()
    except:
        pass
    else:
        print("一个新的客户端到来：%s" % (str(dest_addr)))
        client_list.append((new_socket, dest_addr))

    for new_socket, dest_addr in client_list:
        try:
            recv_data = new_socket.recv(1024)
            recv_data_str = str(recv_data, encoding="utf-8")

        except:
            pass
        else:
            if len(recv_data) > 0:
                new_socket.send(bytes(recv_data_str + "(已读)", encoding="utf-8"))
                print("%s:%s" % (str(dest_addr), recv_data_str))
            else:
                client_list.remove((new_socket, dest_addr))
                new_socket.close()
                print("%s：已下线" % str(dest_addr))
