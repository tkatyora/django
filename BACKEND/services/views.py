from django.shortcuts import render

# Create your views here.

def service(request):
    return render(request, 'service.html')
def projects(request):
    return render(request, 'projects_guides.html')
def products(request):
    return render(request, 'products.html')