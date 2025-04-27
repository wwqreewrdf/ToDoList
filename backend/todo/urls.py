from django.urls import path
from .views import *

todo_patterns = [
    path('table/', TableAPI.as_view()),
    path('group/', GroupAPI.as_view()),
    path('task/', TaskAPI.as_view()),
]