from django.conf.urls import url
from django.views.generic import ListView, DetailView, CreateView
from . import views
from .views import *
from .models import Board, AttFile

urlpatterns = [
    url(r'^list$', ListView.as_view(model=Board), name='list'),
    url(r'^write$', views.writeBoard, name='write'),
]