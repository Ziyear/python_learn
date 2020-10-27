import gevent
from gevent import socket, monkey

monkey.patch_all()


def handler_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print("recv:", str(data, encoding="utf-8"))
        conn.send(data)


def server(port):
    s = socket.socket()
    s.bind(("", port))
    s.listen(5)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handler_request, cli)


if __name__ == '__main__':
    server(7788)
