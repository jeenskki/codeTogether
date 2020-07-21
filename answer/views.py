from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.template import loader
from .models import Answer
# Create your views here.
# def index(request):
#  return HttpResponse("지금 답변하시려면 아래 답변하기를 눌러주세요.")


# 답변하기 누른 경우 보이는 화면 
# def answer_write(request):
#     if not request.session.get('user'):
#         return redirect('/users/login')

#     if request.method == "GET":
#         form = ()

#     elif request.method == "POST":
#         form = BoardForm(request.POST)
#         if form.is_valid():
#             user_id = request.session.get('user')
#             user = Users.objects.get(pk = user_id)
#             new_board = Board(
#                 title = form.cleaned_data['title'],
#                 contents = form.cleaned_data['contents'],
#                 writer = user
#             )
#             new_board.save()
#             return redirect('/board/list')

#     return render(request, 'board_write.html', {'form' :form})


def index(request):
    
    return render(request,'answer/index.html')
    #템플릿 안에, 엔서 안에, 인덱스라서 이렇게 적음

def anslist(request):
    latest_question_list = Answer.objects.order_by('-pub_date')[:10]
    # output = ', '.join([q.question_text for q in latest_question_list])
    return render(request,'answer/anslist.html',{'latest_question_list':latest_question_list})
# latest~~는 딕셔너리 형태로 (키를 줄건데, 벨류값은 뒤에 있는 애) HTML에 준다. 전달한다. 



# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))