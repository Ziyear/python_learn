def say_hello():
    return "hello"


def application(request, response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    response(status, headers)
    return "hello"
