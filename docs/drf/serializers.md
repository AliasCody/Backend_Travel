# What is Serializer?
> <span style='font-size:24px;'>Think of REST as the interface specification, and the serializer as the implementation engine that handles data conversion and validation to satisfy those requirements.</span>

<span style='font-size:24px;font-family:Segoe Print'>There are two major work of a serializer :</span>

<span style='font-size:24px;font-family:Segoe Print'>1. JSON -> Python/Model</span>

<span style='font-size:24px;font-family:Segoe Print'>2. Model -> JSON</span>

# How to declaring serializers?
<span style='font-size:24px;'>Reference: [Serializers](https://www.django-rest-framework.org/api-guide/serializers/#serializers)</span>   


<span style='font-size:24px;font-family:Segoe Print'>In the beginning,we will first have or define the messege's structure,format or else basic info.</span>

<span style='font-size:24px;font-family:Segoe Print'>In the following example,I define the `Comment` object and `CommentSerializer` serializer.(`Comment` is just an simple object with 3 attribute : email,content and created)</span>

<span style='font-size:24px;'>The task : </span>

```python
from datetime import datetime

class Comment: # <-------------- define a class call Comment
    def __init__(self,email,content,created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='cody@hello.com',content='foo bar') # <-------- we initial an Comment object
```

<span style='font-size:24px;'>Declare a serializer :</span>

```python
from rest_framework import serializers 

class CommentSerializer(serializer.Serializer): # <----------------- define a serializer class call CommentSerializer
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

<span style='font-size:24px;'>Serializing the objects :</span>

```python
serializer = CommentSerializer(comment)
serializer.data     # it will be {'email':...,'content':...,'created':...}
```

<span style='font-size:24px;'>Deserializing objects :</span>

```python
import io
from rest_framework.parsers import JSONParser

stream = io.BytesIO(json)
data = JSONParser().parse(stream)
```

# Why user is not in Field?

```python
# Define the serializer to serialize Todo class
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title','created_at'] # prohibit frontend deliever the 'user' data
```

<span style='font-size:24px;font-family:Segoe Print'>1. user comes from authentication</span>

<span style='font-size:24px;font-family:Segoe Print'>2. user should not be controlled by client</span>

<span style='font-size:24px;font-family:Segoe Print'>3. ownership is a system responsibility</span>

# Data Flow: Create Todo

<span style='font-size:24px;'>Client JSON -> Serializer(validate fields) -> View(bind request.user) -> Serializer.create() -> Model -> DB</span>