from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(("", 8899))

server_socket.listen(5)

# client_socket 表示新的客户端
# client_info 表示这个新的客户端的ip及port
client_socket, client_info = server_socket.accept()

socket_recv = client_socket.recv(1024)

print("%s:%s" % (str(client_info), str(socket_recv, encoding="utf-8")))

client_socket.send(bytes("已读", encoding="utf-8"))

client_socket.close()
server_socket.close()
