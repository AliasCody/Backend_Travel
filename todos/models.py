'''
    "model" is the file which defines the structure of data base
'''

from django.conf import settings
from django.db import models

'''
    class Todo: inherit from Django's models.Model
    columns:
        title : stored Todo list's title (CharField)
        created_at : stored time messege (DateTimeField)
        user : Relationship column, it will be connected to someone (ForeignKey)
'''

class Todo(models.Model):

    # attribute
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) # if the data is first created,it will fill the time automatically by the machine.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, # connect to system's list of user
        on_delete=models.CASCADE, # CASCADE follow the rule: if the user has been deleted,the Todo list belongs to who will also be deleted.
        related_name = "todos"    # you can use user.todos.all() to access all the user's Todo list
    )

    # prepare for developer,if you print this object in admin or terminal,you will see the title.
    def __str__(self):
        return self.title
    
from rest_framework import serializers
from .models import Todo

'''
    ModelSerializer is a Mixture of Model and Serializer
    It will generate columns depends on Model,and remain the data structure.
'''


# Define the serializer to serialize Todo class
# Inherit from ModelSerializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo                         # setting this Serializer is responsible for all Todo model
        fields = ['id','title','created_at'] # permit which column in model can interact with API