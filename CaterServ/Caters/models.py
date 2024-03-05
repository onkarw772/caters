from django.db import models
class User(models.Model):
    uid=models.IntegerField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)
    

# Create your models here.
