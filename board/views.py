import json
from django.shortcuts import render
from .models import Board
from django.http import HttpResponse, JsonResponse
from django.views import View

def write(request):
  return render(request, 'board/write.html')

# Create your views here.
def writeBoard(request):
  account_id = request.POST.get('account_id')
  title = request.POST.get('title')  
  content= request.POST.get('content')
  img = request.POST.get('img')
  content_type = request.POST.get('content_type')
  # account_id랑 content_type은 게시글 작성 버튼 누를 때 함께 넘겨야 함

  try:
    Board(
      account_id = account_id,
      title = title,
      content = content,
      img = img,
      content_type = content.type
    ).save()

    return HttpResponse(status= 200)
  except Exception as e:
    return JsonResponse({"message": "오류 발생"}, status = 400)

def boardView(request) :
  c_list = Board.objects.order_by('-content_id')
  return render(request, 'board/board.html', {
    'b_list': b_list,
  })