from django.urls import path
from . import views

# django looks for this variable
# URLConf (URL Configuration Module)
urlpatterns = [
    path('hello', views.say_hello)
]
