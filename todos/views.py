from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer

# define an view which responsible for HTTP request
class TodoCreateView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self,request):
        serializer = TodoSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(user=request.user)
        return Response(serializer.data)