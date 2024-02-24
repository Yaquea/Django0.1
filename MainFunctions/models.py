from django.db import models

# Create your models here.
class Personas(models.Model):

    Nombres= models.CharField(max_length= 15)
    Apellidos= models.CharField(max_length= 15)
    Edad= models.IntegerField()