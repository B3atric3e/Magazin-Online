from django.db import models
from django import forms


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083, blank=True)

