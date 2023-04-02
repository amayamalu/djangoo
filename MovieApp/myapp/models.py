from django.db import models
# from django.contrib.auth.models import User


class Movie(models.Model):
    name=models.CharField(max_length=250)
    year=models.PositiveIntegerField()
    genres=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    runtime=models.CharField(max_length=100)
    poster_pic=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name


