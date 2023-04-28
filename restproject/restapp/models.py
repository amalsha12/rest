from django.db import models
class Specials(models.Model):
    fname=models.CharField(max_length=250)
    fimg=models.ImageField(upload_to='pics')
    fdesc=models.TextField()


class Varieties(models.Model):
    images=models.ImageField(upload_to='pictures')

# Create your models here.
