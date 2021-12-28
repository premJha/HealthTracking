from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Disease(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    keywords = models.CharField(max_length=200)

    def __str__(self):
        return self.name + "{ "+f'{self.keywords}' +" } "


