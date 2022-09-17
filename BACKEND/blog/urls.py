from django.urls import path
from . import views

urlpatterns = [

    path('',views.currentBlog, name = 'currentBlog'),
    path('oldBlog',views.oldBlog, name = 'oldBlog'),
    path('mostLikedBlogs',views.mostLikedBlog, name = 'mostLikedBlog'),
]