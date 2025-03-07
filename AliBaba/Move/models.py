from django.db import models


# Create your models here.

class Reservation(models.Model):
    isReturn = models.BooleanField() 
    date = models.DateTimeField()
    price = models.BigIntegerField()
    transport = models.CharField()
    
    
class Passenger(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=20)
    info = models.ForeignKey(to=Reservation)


class Info(models.Model):
    city = models.CharField(max_length=100)
    reservation = models.ForeignKey(to= Reservation)
    date = models.DateTimeField()


class Train(models.Model):
    is_from = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    passengers = models.ForeignKey(to = Passenger, on_delete=models.CASCADE)
    duration = models.TimeField()
    name = models.CharField(max_length=20)


class Airplane(models.Model):
    is_from = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    passengers = models.ForeignKey(to = Passenger, on_delete=models.CASCADE)
    duration = models.TimeField()
    name = models.CharField(max_length=20)


class Bus(models.Model):
    is_from = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    passengers = models.ForeignKey(to = Passenger, on_delete=models.CASCADE)
    duration = models.TimeField()
    name = models.CharField(max_length=20)
    