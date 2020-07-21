import json
from django.shortcuts import render
from .models import Accounts
from django.http import JsonResponse, HttpResponse
from django.views import View

def index(request):
    return render(request,'sign/signup_main.html')
    

#회원가입 기능

def regist_user(request):
    user_id = request.POST.get('user_id')
    user_pw = request.POST.get('user_pw')
    re_user_pw = request.POST.get('re_user_pw')
    user_name = request.POST.get('user_name')
    user_email = request.POST.get('email')
    user_type = int(request.POST.get('user_type'))
    if user_pw == re_user_pw:
        try:
             if Accounts.objects.filter(user_id = user_id).exists() :
                 return JsonResponse({"message" : "USER_ALREADY_EXIST"}, status = 401)
            Accounts(
                user_id=user_id,
                user_pw=user_pw,
                user_name =user_name,
                email = user_email,
                user_type=user_type
            ).save()
            return render(request, 'main/index.html')
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)
    else: HttpResponse("비밀번호 틀림")
#get 방식으로 요청시 db에 있는 데이터와 함게 
def get_tea(request):
    return render(request,'sign/signup_tea.html',{'user_type':1})

def get_stu(request):
    return render(request,'sign/signup_stu.html',{'user_type':0})

#로그인 기능

def login_chk(request):
    user_id = request.POST.get('user_id')
    user_pw = request.POST.get('user_pw')
    try:
        if Accounts.objects.filter(user_id = user_id).exists() :
            if user_pw == Accounts.objects.get(user_id=user_id).user_pw:
                user_type = User.objects.get(user_id).user_type
                return HttpResponse('0')
            return HttpResponse('1')
        return HttpResponse('2')
    except KeyError:
        return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)
    
    # return HttpResponse(user_id)
def login(request):
    return render(request, 'sign/signin.html')