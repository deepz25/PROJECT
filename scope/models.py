from django.db import models
import datetime



# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.name

class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(max_length=8)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=15)
    hobbies = models.CharField(max_length=50)
    
    

