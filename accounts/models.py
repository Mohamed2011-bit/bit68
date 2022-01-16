from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")

    name =  models.CharField(max_length=100)
    price =  models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        
