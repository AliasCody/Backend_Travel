# Request stream
```
Client

  ↓ POST /todos/

urls.py

  ↓

views.py (TodoCreateView.post)

  ↓

serializers.py (TodoSerializer)

  ↓

models.py (Todo)

  ↓

Response

```

<span style='font-size:24px;'>1. In `urls.py`</span> 

```python
# todos/urls.py
from django.urls import path
from .views import TodoCreateView

urlpatterns = [
   path("todos/", TodoCreateView.as_view()),
]
```

<span style='font-size:24px;'>In `urlpatterns` its clearly tell you if someone request for " todos/ ",than pass the task to `TodoCreateView`.</span>

<span style='font-size:24px;'>2. `views.py`</span>
```python

# todos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer

class TodoCreateView(APIView):
    def post(self, request): # <--
        serializer = TodoSerializer(data=request.data) # <--

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        todo = serializer.save(user=request.user)
        return Response({"id": todo.id}, status=201)

```

<span style='font-size:24px;'>Because client use `HTTP POST`, Django will call `post()` automatically for you.Thats why you need to `def post()`,`request.data` will be a JSON file.</span>

<span style='font-size:24px;'>3. `serializer.py`</span>

```python
# todos/serializers.py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "created_at"]
```