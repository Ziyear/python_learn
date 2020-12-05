from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# url
def index(request):
    return HttpResponse("hello world")


def detail(request, p1, p2, p3):
    return HttpResponse('year:%s,month:%s,day:%s' % (p1, p2, p3))


def show(request, **kwargs):
    return HttpResponse('path: %s , method: %s ' % (request.path, request.method))


def year(request, **kwargs):
    return HttpResponse("year:" + str(kwargs['year']))


# get
def getTest1(request):
    return render(request, 'booktest/getTest1.html')


def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a': a1, 'b': b1, 'c': c1}
    return render(request, 'booktest/getTest2.html', context)


def getTest3(request):
    # a1 = request.GET['a']
    # context = {'a': a1}
    a1 = request.GET.getlist('a')
    context = {'a': a1}
    return render(request, 'booktest/getTest3.html', context)


# post
def postTest1(request):
    return render(request, 'booktest/postTest1.html')


def postTest2(request):
    username = request.POST['username']
    password = request.POST['password']

    gender = request.POST['gender']
    hobby = request.POST.getlist('hobby')
    context = {'username': username, 'password': password, 'gender': gender, 'hobby': hobby}

    return render(request, 'booktest/postTest2.html', context)


# cookie
def cookieTest(request):
    response = HttpResponse()
    cookies = request.COOKIES
    if 't1' in cookies:
        response.write(cookies['t1'])

    # response.set_cookie('t1', 'abc')
    return response


# 重定向
def redirectTest1(request):
    # return HttpResponseRedirect('/booktest/redTest2/')
    return redirect('/booktest/redTest2/')


def redirectTest2(request):
    return HttpResponse('redirectTest2')


# session
def session1(request):
    userName = request.session.get('username')
    context = {'user': userName}
    return render(request, "booktest/session1.html", context)


def session2(request):
    return render(request, "booktest/session2.html")


def session3(request):
    # 删除session
    del request.session['username']
    return redirect("/booktest/session1/")


def login(request):
    request.session['username'] = request.POST['username']
    return redirect("/booktest/session1/")
