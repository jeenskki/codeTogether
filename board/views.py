import json
import os
import requests
from django.shortcuts import render
from .models import Board
from django.http import HttpResponse, JsonResponse
from django.views import View
from sign.models import Accounts

def write(request):
  return render(request, 'board/upload.html')

# Create your views here.
def writeBoard(request):
  user_id = request.session['user_id']
  title = request.POST.get('title')  
  content= request.POST.get('content')
  img = request.FILES['img']
  content_type = request.session['user_type']
  # account_id랑 content_type은 게시글 작성 버튼 누를 때 함께 넘겨야 함
  
  account = Accounts.objects.get(user_id=user_id)
  Board(
    user_id = account,
    title = title,
    content = content,
    img = img,
    content_type = content_type
  ).save()

  # 

  return HttpResponse(status= 200)
  # except Exception as e:
  #   return JsonResponse({"message": "오류 발생"}, status = 400)

def boardView(request) :
  b_list = Board.objects.order_by('-content_id')
  return render(request, 'board/board.html', {
    'b_list': b_list,
  })

def q_stu(request):
  return render(request, 'board/q_stu.html')
 
def save_session(request, user_id, user_type):
  request.session['user_id'] = user_id
  request.session['user_type'] = user_type

def lesson(request) :
  lesson_id = request.GET['lesson_id']
  feed = Board.objects.filter(content_id=lesson_id)
  return render(request, 'board/lesson.html', {
    'contents': feed,
  })

def board_stu(request):
  b_list = Board.objects.order_by('-content_id')
  return render(request, 'board/stu.html', {
    'lists': b_list,
  })

def youtube(request) :
  py_raw = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&q=파이썬&key=AIzaSyB1bUXFvdnJQb1gjpb7eDqPnZhXKxa7qm0')
  j_raw = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&q=자바&key=AIzaSyB1bUXFvdnJQb1gjpb7eDqPnZhXKxa7qm0')
  if py_raw.status_code == 200 :
    py_raw.encoding = "utf-8"
    py_data = py_raw.json()

  if j_raw.status_code == 200 :
    j_raw.encoding = "utf-8"
    j_data = j_raw.json()


  return render(request, 'board/youtube.html', {
    'py_data' : py_data,
    'j_data' : j_data,
  })

  
  
