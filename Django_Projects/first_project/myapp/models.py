from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    created = models.DateField()
      