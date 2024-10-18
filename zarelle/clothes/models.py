from django.db import models

# Create your models here.
class Clothes(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.CharField(max_length=300)
    image2 = models.CharField(max_length=300)
    image3 = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=0)

    def __str__(self):
        return self.name
    
class Price(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=0)
    profit = models.DecimalField(max_digits=20, decimal_places=0)
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.price