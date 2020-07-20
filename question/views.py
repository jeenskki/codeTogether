from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def writeBoard(request) :
  if request.method == 'POST':
    board_form = MyBoardForm(request.POST, instance=Board())
    attfile_forms = [MyAttFileForm(request.POST, request.FILES, instance=AttFile())]
    if board_form.is_valid() and all( [attfile_elem.is_valid() for attfile_elem in attfile_forms]):
      saved_board = board_form.save()
      for attfile_form_elem in attfile_forms:
        new_attfile =  attfile_form_elem.save(commit=False)
        new_attfile.board = saved_board
        new_attfile.save()
      return HttpResponseRedirect('/board/list')
  else:
    board_form = MyBoardForm(instance = Board())
    attfile_form = MyAttFileForm(instance = AttFile())
  return render(request, 'question/board_write.html', {
    'board_form': board_form,
    'attfile_form': attfile_form,
    })

