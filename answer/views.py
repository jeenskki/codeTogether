from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.template import loader
from .models import Answer,Blog
# Create your views here.

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
# 선생님이 작성한 게시글 
def answerdetail(request):
    teacher_id=request.POST.get('teacher_id')
    teacher_title=request.POST.get('teacher_title')
    teacher_content=request.POST.get('teacher_content')
    teacher_image=request.POST.get('teacher_image')
    pub_date =request.POST.get('--------')

def index(request):   
    return render(request,'answer/index.html')
    #템플릿 안에, 엔서 안에, 인덱스라서 이렇게 적음

def answerlist(request):
    latest_question_list = Answer.objects.order_by('-pub_date')[:10]
    # output = ', '.join([q.question_text for q in latest_question_list])
    return render(request,'answer/anslist.html',{'latest_question_list':latest_question_list})
# latest~~는 딕셔너리 형태로 (키를 줄건데, 벨류값은 뒤에 있는 애) HTML에 준다. 전달한다. 

def new_ans(request):
    return render(request, 'write_ans.html')

# 글 작성 요청이 들어오면 객체 생성해서 데이터에 값을 넣어줌
def create(request):

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))