from django.db import models

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=20)
    
    
class Airplane(models.Model):pass


class Info(models.Model):
    city = models.CharField(max_length=100)
    reservation = models.ForeignKey(to= Reservation)
    date = models.DateTimeField()


class Bus(models.Model):
    passenger = models.ForeignKey(to= Passenger, on_delete= models.CASCADE)


class Train(models.Model):
    Passenger = models.ForeignKey(to= Passenger, on_delete= models.CASCADE)

