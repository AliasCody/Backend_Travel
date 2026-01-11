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