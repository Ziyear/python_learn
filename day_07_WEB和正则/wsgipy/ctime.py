import time


def say_time():
    return time.ctime()


def application(request, response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    response(status, headers)
    return time.ctime()
