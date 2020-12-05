from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("show", views.show, name='show'),
    re_path(r"^(\d+)$", views.show_re, name='show_re'),

    path("index2", views.index2, name='index2'),
    path("user1", views.user1, name='user1'),
    path("user2", views.user2, name='user2'),
    path("htmlTest", views.htmlTest, name='htmlTest'),

    path("csrf1", views.csrf1, name='csrf1'),
    path("csrf2", views.csrf2, name='csrf2'),
]
