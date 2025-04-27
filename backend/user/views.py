from django.forms import model_to_dict
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response


class UserCreate(APIView):
    
    def post(self, request):
        new_user = User.objects.create_user(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )
        return Response({'post': model_to_dict(new_user)})
    

class UserLogin(APIView):

    def post(self, request):
        pass