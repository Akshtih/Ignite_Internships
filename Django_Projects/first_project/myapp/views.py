from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    return render(request,'1.html')
def aboutme(request):
    items = models.ToDoItem.objects.all()
    return render(request,'aboutme.html',{'items':items})
def Women(request):
    return render(request,'Women.html')
def art(request):
    return render(request,'art.html')

