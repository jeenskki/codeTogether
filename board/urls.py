from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('write/', views.write),
    path('', views.boardView),
    path('writeBoard/',views.writeBoard),
    path('q_stu/', views.q_stu),
]
