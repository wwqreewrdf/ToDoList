from ..models import Group

from rest_framework.views import APIView
from rest_framework.response import Response


class GroupAPI(APIView):

    def post(self, request):
        data = request.data

        Group.objects.create(
            name=data['name'],
            table_id=data['table_id'],
            color=data['color'])
        return Response(data)

    def patch(self, request):
        data = request.data

        Group.objects.filter(id=data['id']).update(
            name=data['name'],
            color=data['color']
        )
        return Response(data)

    def delete(self, request):
        data = request.data
        Group.objects.delete(id=data['id'])
        return Response(data)
