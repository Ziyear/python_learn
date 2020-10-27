from socket import *
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./html"


def handle_cli(client_socket, client_addr):
    """处理客户端请求"""
    request_data = client_socket.recv(1024)
    request_data_str = str(request_data, encoding="utf-8")
    if request_data_str == "":
        client_socket.close()
        print("[%s]关闭了链接" % (str(client_addr)))
        return
    request_lines = request_data_str.splitlines()
    for line in request_lines:
        print(line)

    # 解析报文
    req_start_line = request_lines[0]
    # 获取文件名
    file_name = re.match(r"\w+ +(/[^ ]*) ", req_start_line).group(1)
    if file_name == "/":
        file_name = "/index.html"
    # 打开文件
    try:
        file = open(HTML_ROOT_DIR + file_name, "rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 NOT Found\r\n"
        response_headers = "Server: My server \r\n"
        response_body = "This file is not found!"
    else:
        file_data = file.read()
        file.close()

        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server \r\n"
        response_body = file_data.decode("utf-8")
    response = response_start_line + response_headers + "\r\n" + response_body
    client_socket.send(bytes(response, encoding="utf-8"))
    print("接收到请求：%s" % request_data_str)
    print("响应的数据：%s" % response)
    client_socket.close()


if __name__ == '__main__':
    ser_socket = socket(AF_INET, SOCK_STREAM)
    ser_socket.bind(("", 8000))
    ser_socket.listen(128)
    while True:
        cli_socket, cli_addr = ser_socket.accept()
        print("[%s]用户连接上了" % (str(cli_addr)))
        handle_cli_socket_process = Process(target=handle_cli, args=(cli_socket, cli_addr))
        handle_cli_socket_process.start()
