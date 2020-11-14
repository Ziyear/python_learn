from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from .models import *


# Create your views here.

def index(request):
    # template = loader.get_template("booktest/index.html")
    # return HttpResponse(template.render())
    objects_all = BookInfo.objects.all()
    content = {'title': "Hello World    hahahha", "list": objects_all}
    return render(request, 'booktest/index.html', content)
