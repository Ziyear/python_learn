from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('myexp', views.my_exp),
    path('uploadPic', views.upload_pic),
    path('uploadHandle', views.upload_handler),
    path('heroList', views.heroList),
    path('areaPage', views.areaPage),
    path('area', views.areas),

]
