from django.urls import path
from . import views

urlpatterns = [
  path("", views.LogIn, name="LogIn"),
  path("Regestration", views.regester , name="regester")
  
]