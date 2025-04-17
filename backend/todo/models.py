from django.db import models
from user.models import User


class Table(models.Model):
    name = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.TextField(default="")
    position = models.SmallIntegerField(default=0)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default="")

    color = models.TextField(default="")

class Task(models.Model):
    name = models.TextField(default="")
    description = models.TextField(default="")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default="")

    color = models.TextField(default="")
