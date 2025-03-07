from django.db import models

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=20)
    
    
class Airplane(models.Model):


class 