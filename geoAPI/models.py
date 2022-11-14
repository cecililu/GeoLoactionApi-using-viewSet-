from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=30)
    lat = models.CharField(max_length=30)
    long = models.CharField(max_length=30)
    
