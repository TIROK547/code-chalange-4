from django.db import models


# Create your models here.

class Reservation(models.Model):
    isReturn = models.BooleanField() 
    date = models.DateTimeField()
    price = models.BigIntegerField()
    is_airplane = models.ForeignKey(to = "Airplane",related_name="Airplane", on_delete= models.CASCADE)
    is_train = models.ForeignKey(to = "Train",related_name="Bus", on_delete= models.CASCADE)
    is_Bus = models.ForeignKey(to = "Bus",related_name="Train", on_delete= models.CASCADE)
    info = models.ForeignKey(to="Passenger",related_name="Passenger",on_delete= models.CASCADE)
    
    
class Passenger(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=20)
    email = models.EmailField()


class Train(models.Model):
    is_from = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    duration = models.TimeField()
    name = models.CharField(max_length=20)
    


class Airplane(models.Model):
    is_from = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    duration = models.TimeField()
    name = models.CharField(max_length=20)


class Bus(models.Model):
    is_from = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    duration = models.TimeField()
    name = models.CharField(max_length=20)
    
    
