from django.urls import path
from . import views

urlpatterns = [
  path("", views.Login, name="Login"),
  
  path("Regestration", views.regester , name="regester")
  
]

