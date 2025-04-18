from django.contrib.admindocs.utils import named_group_matcher
from django.urls import path, re_path
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.home,name='home'),
    path('home/', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('<str:short>',views.direct,name='direct'),
    path('?longurl=<str:longurl>',views.getdata,name='getdata'),
    path('aftershort<lurl>/',views.aftershort,name='aftershort'),
]