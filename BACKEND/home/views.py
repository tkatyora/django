from django.shortcuts import render
from .models import HomeCarousel, Introduction

# Create your views here.
Introduction = Introduction.objects.all() # creating a list of introductions


def home(request):
    content ={}
    content={
      'Introduction' :Introduction 
    }
    return render(request , 'index.html' , content)
def about(request):
    return render(request , 'about.html')

def projects(request):
     return render(request , 'projects.html')
 
 
 
 
 
 
 
# hard coding the data
#services= HomeService()
# services.header = 'Web Development'
# services.Discription =  'We Offer Good Services'
# services.Button = 'servicess'

# # the produects
# products= HomeService()
# products.header = 'Products'
# products.Discription =  'We sell cool and nice products'
# products.Button = 'products'

# #projects guides
# projects_guides= HomeService()
# projects_guides.header ='projects'
# projects_guides.Discription =  'We offer help in project planning and management'
# projects_guides.Button = 'projects'

# #addding the list manually
# # Homeservices  = [services,products,projects_guides]

    