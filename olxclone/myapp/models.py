from django.db import models

class Vehicles(models.Model):
    name=models.CharField(max_length=250)
    model=models.CharField(max_length=250)
    category=models.CharField(max_length=250)
    owner_type=models.CharField(max_length=250)
    fuel_type=models.CharField(max_length=250)
    kms=models.CharField(max_length=250)
    price=models.PositiveIntegerField()
    number=models.CharField(max_length=200,unique=True)
    description=models.CharField(max_length=2550)

    def __str__(self):
        return self.name


class Mobiles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    display=models.CharField(max_length=150,default="lcd")

    def __str__(self):
        return self.name
    


class Cinema(models.Model):
    name=models.CharField(max_length=250)
    genres=models.CharField(max_length=250)
    year=models.PositiveIntegerField()
    language=models.CharField(max_length=100)
    rating=models.PositiveIntegerField()

    def __str__(self):
        return self.name
