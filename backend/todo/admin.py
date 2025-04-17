from django.contrib import admin

from .models import Task, Group, Table


admin.register(Table)
admin.register(Task)
admin.register(Group)