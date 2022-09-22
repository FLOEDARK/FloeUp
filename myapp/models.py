from django.db import models

# Create your models here.

class Feature(models.Model):
    name= models.CharField(max_length = 100)
    details= models.CharField(max_length = 1000)


class About(models.Model):
    about= models.CharField(max_length = 50)
    details= models.CharField(max_length = 1000)

class FloeAbout(models.Model):
    offer= models.CharField(max_length= 500)
    ofdetails= models.CharField(max_length= 1000)

class Contact(models.Model):
    company= models.CharField(max_length= 20)
    email= models.CharField(max_length= 50)
    phone= models.CharField(max_length= 30)

   

