import json
from django.shortcuts import render
from .models import User
from django.http import JsonResponse, HttpResponse
from django.views import View
#회원가입 기능
class SignUpView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        re_user_pw = request.POST.get('re_user_pw')
        username = request.POST.get('username')
        user_email = request.POST.get('email')
        birth = request.POST.get('birth')
        user_type = request.POST.get('user_type') #user_type을 signup_ 페이지에서 설정후에 가져와야하는데 어떻게 넣어주지

        if user_pw == re_user_pw:
            try:
                if User.objects.filter(user_id = user_id).exists() :
                    return JsonResponse({"message" : "USER_ALREADY_EXIST"}, status = 401)
                User(
                    user_id=user_id,
                    email=email,
                    password=password,
                    username =username,
                    email=user_email,
                    birth=birth,
                    user_type=user_type
                ).save()
                return HttpResponse(status = 200)
            except KeyError:
                return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)
        else: HttpResponse("비밀번호 틀림")
#get 방식으로 요청시 db에 있는 데이터와 함게 
    def get_tea(self, request):
        return render(request,'sign/signup_tea.html')
    
    def get_stu(self, request):
        return render(request,'sign/signup_sut.html')

#로그인 기능
class LoginView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        try:
            if User.objects.filter(user_id = user_id).exists() :
                if user_pw == User.objects.get(user_id=user_id).user_pw:
                    user_type = User.objects.get(user_id).user_type
                    return HttpResponse('0')
                return HttpResponse('1')
            return HttpResponse('2')
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)
       
        # return HttpResponse(user_id)
    def get(self,request):
        return render(request, 'sign/signin.html')