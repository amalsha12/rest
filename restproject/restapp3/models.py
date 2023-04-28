from django.db import models
class Food(models.Model):
    foodday=models.CharField(max_length=25)
    foodname=models.CharField(max_length=250)
    foodimg=models.ImageField(upload_to='pics')
    fooddesc=models.TextField()



    images=models.ImageField(upload_to='pictures')
# Create your models here.
