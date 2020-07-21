import json
from .models import Accounts, t_list
from django.views import View
from django.http import HttpResponse, JsonResponse
# Create your views here.
def signup_main(request):
  return render(HttpResponse(request))

class SignUp(View):
  def post(self, request):
    data = json.loads(request.body)

    try:
      if Accounts.objects.filter(user_id = data['user_id']).exists():
        return JsonResponse({"message": "User already exists"}, status= 400)

      if Accounts.objects.filter(user_pw= data['user_pw']).length() < 4:
        return JsonResponse({"message": "Password is too short"}, status= 400)

      Accounts.objects.create(
        user_id = data['user_id'],
        user_pw = data['user_pw'],
        user_name = data['user_name'],
        email = data['user_email'],
        user_type = data['user_type']
      ).save()

      if Accounts.objects.filter(user_type= data['user_type']) == 1:
        t_list.objects.create(
          field_main = data['field_main'],
          field_sub = data['field_sub'],
        ).save()

      return HttpResponse(status = 200)

    except KeyError:
      return JsonResponse({"message": "Invalid Keys"}, status=400)
