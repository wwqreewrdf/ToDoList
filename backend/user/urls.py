from django.urls import path

from .views import *


user_patterns = [
    path('/all', UserView.as_view())
]
