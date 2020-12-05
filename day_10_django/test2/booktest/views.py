from django.shortcuts import render
from django.db.models import Max
from .models import *


def index(request):
    # list = BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    list = BookInfo.books1.filter(pk__lt=3)
    max = BookInfo.books1.aggregate(Max('bpub_date'))
    content = {'title': "Hello World    hahahha", "list": list,'Max':max}
    return render(request, 'booktest/index.html', content)
