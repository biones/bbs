from django.conf.urls import url,include
from django.urls import path
from . import views

app_name = 'bbs'
urlpatterns = [
    path('', views.index, name='index'),
    path('write', views.write, name='write'),
]
