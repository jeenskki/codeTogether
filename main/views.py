from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from board.models import Board
# Create your views here.
def main(request):
    list = Board.objects.order_by('-content_id')
    return render(request,'main/index.html', {
        'b_list' : list,
    })

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/')