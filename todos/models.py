'''
    "model" is the file which defines the structure of data base
'''

from django.conf import settings
from django.db import models

'''
    Django provides the class "models.Model", which contains tools for storing, deleting, and searching data.
'''

# Compares to ERD, Todo is an Entity
class Todo(models.Model):

    # attribute
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = "todos"
    )

    def __str__(self):
        return self.title
    
from rest_framework import serializers
from .models import Todo

'''
    ModelSerializer is a Mixture of Model and Serializer
    It will generate columns depends on Model,and remain the data structure.
'''


# Define the serializer to serialize Todo class
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title','created_at'] # prohibit frontend deliever the 'user' data