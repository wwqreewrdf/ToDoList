from django.db import models


class User(models.Model):
    login = models.TextField(default="")
    password = models.TextField(default="")

    def __str__(self):
        return self.login