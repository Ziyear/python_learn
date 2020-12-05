from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:year>/', views.year),
    path('show', views.show),
    # re_path(r'(\d+)/(\d+)/(\d+)/$', views.detail),
    re_path(r'(?P<p1>\d+)/(?P<p2>\d+)/(?P<p3>\d+)/$', views.detail),
    path('getTest1/', views.getTest1),
    path('getTest2/', views.getTest2),
    path('getTest3/', views.getTest3),
    path('postTest1/', views.postTest1),
    path('postTest2/', views.postTest2),

    path('cookieTest/', views.cookieTest),

    path('redTest1/', views.redirectTest1),
    path('redTest2/', views.redirectTest2),

    path('session1/', views.session1),
    path('session2/', views.session2),
    path('session3/', views.session3),

    path('login', views.login),
]
