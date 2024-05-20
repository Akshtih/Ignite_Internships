from django.shortcuts import render,redirect
from . import models
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.http import JsonResponse
 
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
def complete(request,id):
    item = models.ToDoItem.objects.get(pk=id)
    item.status = True
    item.save()
    return redirect('aboutme')
def delete(request,id):
    item = models.ToDoItem.objects.get(pk=id)
    item.delete()
    return redirect('aboutme')
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        models.ToDoItem.objects.create(title=title,description=description,created=date)
    return redirect('aboutme')


    


def listallTodoItems(request):
    items = ToDoItem.objects.all()
    serializer = listallTodoItemsserializer(items, many=True)
    return Response(serializer.data)

class listallTodoItems(generics.ListAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = listallTodoItemsserializer

@api_view(['POST'])
def api_add_todo(request):
    serializer = TodoItemCreate(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,status=201)

@api_view(['PUT'])
def change_status(request, pk):
    try:
        todo = ToDoItem.objects.get(pk=pk)
    except ToDoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    todo.status = request.data.get('status', todo.status)
    todo.save()
    serializer = listallTodoItemsserializer(todo)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_todo(request, pk):
    try:
        todo = ToDoItem.objects.get(pk=pk)
    except ToDoItem.DoesNotExist:
        return Response({"message": "TodoItem not found"}, status=status.HTTP_404_NOT_FOUND)
    todo.delete()
    return Response({"message": "TodoItem deleted successfully"}, status=status.HTTP_200_OK)