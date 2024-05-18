from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'1.html')
def aboutme(request):
    return render(request,'aboutme.html')