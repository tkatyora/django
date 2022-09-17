from django.urls import path 
from . import views

urlpatterns = [
  path('' , views.service, name ='service'),  
  path('projects' , views.projects, name ='projects'),  
  path('products' , views.products, name ='products'),  
]
