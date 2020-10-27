from socket import *
from multiprocessing import Process


def handle_cli(client_socket):
    """处理客户端请求"""
    request_data = client_socket.recv(1024)
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server \r\n"
    response_body = "hello my friends"
    response = response_start_line + response_headers + "\r\n" + response_body
    client_socket.send(bytes(response, encoding="utf-8"))
    print("接收到请求：%s" % str(request_data, encoding="utf-8"))
    print("响应的数据：%s" % response)
    client_socket.close()


if __name__ == '__main__':
    ser_socket = socket(AF_INET, SOCK_STREAM)
    ser_socket.bind(("", 8000))
    ser_socket.listen(128)
    while True:
        cli_socket, cli_addr = ser_socket.accept()
        print("[%s]用户连接上了" % (str(cli_addr)))
        handle_cli_socket_process = Process(target=handle_cli, args=(cli_socket,))
        handle_cli_socket_process.start()
