from django.db import models

# Create your models here.


class NewCar(models.Model):
    make = models.CharField(max_length=100)
    m0del = models.CharField(max_length=100)
    year = models.IntegerField(default=2019)
    mpg = models.IntegerField(default=0)


