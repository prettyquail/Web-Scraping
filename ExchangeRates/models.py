from django.db import models

# Create your models here.
class Currency(models.Model):
    country = models.CharField(max_length=5)
    abbrs = models.CharField(max_length=66)
    currencies = models.CharField(max_length=55)
