from django.urls import path 
from .views import Process_commands

urlpatterns = [
    path('send/', Process_commands.as_view()),
   
]
