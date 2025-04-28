from django.forms import model_to_dict
from .models import Table, Group, Task

from rest_framework.views import APIView
from rest_framework.response import Response


class TablesAPI(APIView):

    def get(self, request):
        data = Table.objects.filter(user=request.user).values()
        return Response({'tables': list(data)})
    
    def post(self, request):
        data = request.data
        Table.objects.create(
            name=data['name'],
            user=request.user
        )
        return Response(data)
    
    def patch(self, request):
        data = request.data
        Table.objects.filter(id=data['id']).update(name=data['name'])
        return Response(data)

    def delete(self, request):
        data = request.data
        Table.objects.filter(id=data['id']).delete()
        return Response(data)
    

class TableAPI(APIView):

    def get(self, request, id):
        table = Table.objects.get(user=request.user, id=id)

        groups = Group.objects.filter(table=table)
        tasks = Task.objects.filter(group__in=groups)

        response_data = {
            'table': model_to_dict(table),
            'groups': [model_to_dict(group) for group in groups],
            'tasks': [model_to_dict(task) for task in tasks]
        }

        return Response(response_data)


class GroupAPI(APIView):

    def post(self, request):
        data = request.data

        Group.objects.create(
            name=data['name'],
            user=request.user)
        return Response(data)

    def patch(self, request):
        data = request.data
        Table.objects.filter(id=data['id']).update(name=data['name'])
        return Response(data)

    def delete(self, request):
        pass


class TaskAPI(APIView):

    def post(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass