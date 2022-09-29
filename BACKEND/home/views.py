from django.shortcuts import render


# Create your views here.
class homeservices():
    header:int
    Discription:int 
    Button:int
    # def __init__(self, header:str , discriprition:str,button:str):
    #     self.header = header
    #     self.Discription = discriprition
    #     self.Button = header

services= homeservices()
services.header = 'Web Development'
services.Discription =  'We sell cool and nice products'
services.Button = 'more services'

# the produects
products= homeservices()
products.header = 'Products'
products.Discription =  'We sell cool and nice products'
products.Button = 'more products'

#projects guides
projects_guides= homeservices()
projects_guides.header ='projects'
projects_guides.Discription =  'we offer help in project planning and management'
projects_guides.Button = 'projects'

#projects guides
Homeservices= [services.header,services.Discription,services.Button]
print(type(Homeservices))
for data in Homeservices:
    print(data)
def home(request):
    
    person = ['takdzwa','gracious','carey','nicole']
    content ={}
    content={
        'Homeservice':Homeservices
    }
    return render(request , 'index.html' , content)

def about(request):
    return render(request , 'about.html')

def projects(request):
     return render(request , 'projects.html')
    