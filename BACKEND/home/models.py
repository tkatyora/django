from django.db import models

# Create your models here.
# This is the class responsible for the fist caousel
class HomeCarousel(models.Model):
  Header = models.CharField( max_length=20) 
  Picture = models.ImageField(upload_to='pictures', height_field=None, width_field=None, max_length=None)

  def __str__(self):
        return self.Header
      
      
# this is a class resinsible for the intoduction  sectione 
class Introduction(models.Model):
  Header = models.CharField(max_length=20)
  Picture = models.ImageField(upload_to = 'pictures')
  Discription = models.TextField()
  Buutton = models.CharField( max_length=20)
  
  def __str__(self):
        return self.Header
