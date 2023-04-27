from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
