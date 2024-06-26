from django.db import models

# Create your models here. 
#  varchar== charfield
class category (models.Model):
    name= models.CharField(max_length=255)
    
