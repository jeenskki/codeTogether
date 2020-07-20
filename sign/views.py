import json
from django.shortcuts import render
from .models import User
from django.http import JsonResponse, HttpResponse
from django.views import View
#회원가입 기능
class SignUpView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        try:
            if User.objects.filter(user_id = data['user_id']).exists() :
                return JsonResponse({"message" : "USER_ALREADY_EXIST"}, status = 401)
            User(
                user_id=data['user_id'],
                email=data['email'],
                password=data['password'],
            ).save()
            return HttpResponse(status = 200)
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)
#get 방식으로 요청시 db에 있는 데이터와 함게 
    def get(self, request):
        return render(request,'sign/signup.html')

#로그인 기능
class LoginView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        # print(User.objects.get(user_id=user_id))
        try:
            if User.objects.filter(user_id = user_id).exists() :
                
                if user_pw == User.objects.get(user_id=user_id).user_pw:
                    return HttpResponse('0')
                return HttpResponse('1')
            return HttpResponse('2')
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)\
       
        # return HttpResponse(user_id)
    def get(self,request):
        return render(request, 'sign/signin.html')