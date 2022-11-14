from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    categoryname = models.CharField(max_length=50)
    def __str__(self):
        return self.categoryname



class Person(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    picture = models.FileField(null=True)
    mobileno = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    regdate = models.DateField()
    def __str__(self):
        return self.name





