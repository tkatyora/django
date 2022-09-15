from django.shortcuts import render
from .models import HomeServices

# Create your views here.
def home(request):
    context = {}
    projects = HomeServices()
    projects.header : 'Web Development'
    projects.disc : ' We can Design your front end websites(staic) maintain the frontend websites' 
    projects.button :'products'
    
    products = HomeServices()
    products.header : 'Web Developdment'
    products.disc : ' We can Deesign your front end websites(staic) maintain the frontend websites' 
    products.button :'projects'
    
    service = HomeServices()
    service.header : 'Web Developdment'
    service.disc : ' We can Deesign your front end websites(staic) maintain the frontend websites' 
    service.button :'projects'
    
    
    
    home =[service, projects,products]
    context = {
       'services_header' :'Web development' ,
       'services_disc'   : ' We can Design your front end websites(staic) maintain the frontend websites' ,
       'services_button' :'Services',
       'home':home
    }
   
    
    
   
    return render(request , 'index.html' , context)

def about(request):
    return render(request , 'about.html')

def projects(request):
     return render(request , 'projects.html')
    