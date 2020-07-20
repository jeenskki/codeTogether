from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'sign/signin.html')

def login_post(request):
    user_id = request.GET.get('user_id')
    user_pw = request.GET.get('user_pw')
    print(user_id, user_pw)
    request.session['user_id'] = user_id
    return HttpResponse("로그인 완료")

def logout(request):
    request.session['user_id'] = None
    request.session.clear()
    return HttpResponse("로그아웃")

def singup(request):
    return render(request,'signup.html')

