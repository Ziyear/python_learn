import time
# from MyWebServer import HTTPServer

HTML_ROOT_DIR = "./html"


class Application(object):
    """"""

    def __init__(self, urls):
        # 设置路由信息
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        # /static/index.html
        if path.startswith("/static"):
            file_name = path[7:]
            if file_name == "/":
                file_name = "/index.html"
            # 打开文件
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                status = "HTTP/1.1 404 NOT Found"
                headers = []
                start_response(status, headers)
                return "This file is not found!"
            else:
                file_data = file.read()
                file.close()

                status = "HTTP/1.1 200 OK\r\n"
                headers = []
                start_response(status, headers)
                return file_data.decode("utf-8")
        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)
        # 未找到路由信息
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found!"


def show_ctime(env, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return "hello"


urls = [
    ("/", say_hello),
    ("/ctime", show_ctime),
    ("/sayhello", say_hello)
]
app = Application(urls)
# if __name__ == '__main__':
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()
