from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('write/', views.write),
    path('', views.boardView),
    path('writeBoard/',views.writeBoard),
    path('q_stu/', views.q_stu),
    path('lesson/', views.lesson),
    path('stu/', views.board_stu),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)