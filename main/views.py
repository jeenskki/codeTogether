from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
def index(request):
  return render(HttpResponse(request))
=======
def main(request):
    print(request.method)
    return render(request,'main/index.html')
>>>>>>> 070bb3431ca157d51865756716d5eabf4575ec03
