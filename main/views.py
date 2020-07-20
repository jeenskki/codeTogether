from django.shortcuts import render

# Create your views here.
def main(request):
    print(request.method)
    return render(request,'main/index.html')