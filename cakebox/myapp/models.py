from django.db import models

class Cakes(models.Model):
    name=models.CharField(max_length=250)
    flavour=models.CharField(max_length=250)
    price=models.PositiveIntegerField()
    shape=models.CharField(max_length=250)
    weight=models.CharField(max_length=250)
    layer=models.CharField(max_length=250)
    description=models.CharField(max_length=250,default="null")
    pic=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name
    

    
