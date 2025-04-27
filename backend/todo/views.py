from django.forms import model_to_dict
from .models import Table, Group, Task

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TableAPI(APIView):

    def get(self, request):
        data = Table.objects.filter(user=request.user).values()
        return Response({'tables': list(data)})



class GroupAPI(APIView):

    def get(self, request):
        pass


class TaskAPI(APIView):

    def get(self, request):
        pass