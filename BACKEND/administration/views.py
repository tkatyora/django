from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def LogIn(request):
    return render(request , 'Login.html')
def regester(request):
    return render(request , 'regester.html')
