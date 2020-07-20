import json
from .models import User
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

#회원가입 기능
class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
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
        # users = User.objects.values()
        # data =  JsonResponse({"data" : list(users)}, status = 200)
        return render(request,'sign/signup.html')

#로그인 기능
class LoginView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        try:
            if User.objects.filter(user_id = user_id).exists() :
                if user_pw == User.objects.get(user_id=user_id).user_pw:
                    return HttpResponse(status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=401)
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)
    def get(self,request):
        return render(request, 'sign/signin.html')
            




# Create your views here.
# def login(request):
#     return render(request, 'sign/signin.html')

# def login_post(request):
#     user_id = request.GET.get('user_id')
#     user_pw = request.GET.get('user_pw')
#     print(user_id, user_pw)
#     request.session['user_id'] = user_id
#     return HttpResponse("로그인 완료")

# def logout(request):
#     request.session['user_id'] = None
#     request.session.clear()
#     return HttpResponse("로그아웃")

# def singup(request):
#     return render(request,'signup.html')