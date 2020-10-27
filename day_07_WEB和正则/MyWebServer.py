import re
from multiprocessing import Process
from socket import *
import sys

HTML_ROOT_DIR = "./html"
WSGI_ROOT_DIR = "./wsgipy"


class HTTPServer(object):
    """"""

    def __init__(self, application):
        # 框架的引用
        self.application = application
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def start(self):
        self.server_socket.listen(128)
        while True:
            cli_socket, cli_addr = self.server_socket.accept()
            print("[%s]用户连接上了" % (str(cli_addr)))
            handle_cli_socket_process = Process(target=self.handle_cli, args=(cli_socket, cli_addr))
            handle_cli_socket_process.start()

    def start_response(self, status, headers):
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s:%s\r\n" % header
        self.response_headers = response_headers

    def handle_cli(self, client_socket, client_addr):
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
        method = re.match(r"(\w+) +/[^ ]* ", req_start_line).group(1)

        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }
        response_body = self.application(env, self.start_response)
        response = self.response_headers + "\r\n" + response_body
        client_socket.send(bytes(response, encoding="utf-8"))
        print("接收到请求：%s" % request_data_str)
        print("响应的数据：%s" % response)
        client_socket.close()

    def bind(self, port):
        self.server_socket.bind(("", port))


def main():
    if len(sys.argv) < 2:
        sys.exit("python MyWebServer.py Module:app")
    module_name, app_name = sys.argv[1].split(":")
    m = __import__(module_name)
    app = getattr(m, app_name)
    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start()


# MyWebFramework:app
if __name__ == '__main__':
    main()
