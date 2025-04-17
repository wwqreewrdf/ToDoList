from django.db import models


class User(models.Model):
    login = models.TextField(default="")
    password = models.TextField(default="")
