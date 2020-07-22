import json
from django.shortcuts import render
from .models import Accounts
from django.http import JsonResponse, HttpResponse
from django.views import View

def index(request):
    return render(request,'sign/signup_main.html')
    

#회원가입 기능

def regist_user(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_name = request.POST['user_name']
        user_email = request.POST['email']
        user_type = request.POST['user_type']

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
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        if Accounts.objects.filter(user_id=user_id).exists():
            if user_pw == Accounts.objects.get(user_id=user_id).user_pw :
                user_type = Accounts.objects.get(user_id=user_id).user_type
                save_session(request, user_id, user_type)
                return HttpResponseRedirect('answer/index/')
            else:
                return JsonResponse({'error':"Incorrect Password."}, status=400)
        else:
            return JsonResponse({'error': "아이디가 없습니다."}, status=400)

    # user_id = request.POST.get('user_id')
    # user_pw = request.POST.get('user_pw')
    # try:
    #     if Accounts.objects.filter(user_id = user_id).exists() :
    #         if user_pw == Accounts.objects.get(user_id=user_id).user_pw:
    #             user_type = User.objects.get(user_id).user_type
    #             return HttpResponse('0')
    #         return HttpResponse('1')
    #     return HttpResponse('2')
    # except KeyError:
    #     return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)
    
    # return HttpResponse(user_id)
def login(request):
    return render(request, 'sign/signin.html')

def save_session(request, user_id, user_type):
    request.session['user_id'] = user_id
    request.session['user_type'] = user_type