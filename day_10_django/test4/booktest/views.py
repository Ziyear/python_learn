from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    hero = HeroInfo.objects.get(pk=1)
    list = HeroInfo.objects.all()
    context = {"hero": hero, 'list': list}
    return render(request, 'booktest/index.html', context)


def show(request, id=None):
    context = {'id': id}
    return render(request, 'booktest/show.html', context)


def show_re(request, id):
    context = {'id': id}
    return render(request, 'booktest/show.html', context)


def index2(request):
    context = {}
    return render(request, 'booktest/index2.html', context)


def user1(request):
    context = {'username': '张大胆'}
    return render(request, 'booktest/user1.html', context)


def user2(request):
    context = {}
    return render(request, 'booktest/user2.html', context)


# html转义
def htmlTest(request):
    context = {'t1': '<h1>h1</h1>'}
    return render(request, 'booktest/htmlTest.html', context)


# csrf 跨站
def csrf1(request):
    context = {}
    return render(request, 'booktest/csrf1.html', context)


def csrf2(request):
    username_ = request.POST['username']
    return HttpResponse(username_)
