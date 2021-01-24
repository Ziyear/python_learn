from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import *
import os


# Create your views here.

def index(request):
    return render(request, 'booktest/index.html')


def my_exp(request):
    i = 1 / 0
    return HttpResponse('hello')


def upload_pic(request):
    return render(request, 'booktest/uploadPic.html')


def upload_handler(request):
    pic1 = request.FILES['pic1']
    pic_name = os.path.join(settings.MEDIA_ROOT, pic1.name)
    default_storage.save(pic_name, ContentFile(pic1.read()))
    return HttpResponse('<img src="/static/media/%s" />' % pic1.name)


def heroList(request):
    page_index = request.GET.get("index")
    if page_index:
        page_index = int(page_index)
    else:
        page_index = 1
    list = HeroInfo.objects.all()
    paginator = Paginator(list, 5)
    page = paginator.page(page_index)
    context = {'page': page}
    return render(request, 'booktest/heroList.html', context)


def areaPage(request):
    return render(request, 'booktest/area.html')


def areas(request):
    level = request.GET.get("level")
    parea_id = request.GET.get("pid")

    if parea_id:
        parea_id = int(parea_id)

    if level:
        level = int(level)
    else:
        level = 1
    if level > 3 or level < 1:
        raise Exception("错误的省市区级别")
    if level == 1:
        data = AreaInfo.objects.filter(level_id=level)
    elif parea_id is None:
        raise Exception("市区级别上一级不能为空")
    else:
        data = AreaInfo.objects.filter(level_id=level, parea_id=parea_id)

    list = []
    for area in data:
        list.append([area.id, area.title])
    return JsonResponse({'data': list})
