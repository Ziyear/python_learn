from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyException(MiddlewareMixin):
    def process_exception(request, response, exception):
        return HttpResponse(exception)
