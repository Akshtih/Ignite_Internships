from rest_framework import serializers
from .models import ToDoItem

class listallTodoItemsserializer(serializers.ModelSerializer):
    class Meta:
        model=ToDoItem
        fields = '__all__'


class TodoItemCreate(serializers.ModelSerializer):
    class Meta:
        model=ToDoItem
        fields = ['title','description','created','status']