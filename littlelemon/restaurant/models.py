from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField()
    BookingDate = models.DateField()
    


# Add code to create Menu model
class Menu(models.Model):
   Title = models.CharField(max_length=255) 
   Price = models.DecimalField(max_digits=10,decimal_places=2) 
   Inventory = models.SmallIntegerField()

   def __str__(self):
     return f'{self.Title} : {str(self.Price)}'
