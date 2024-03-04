from django.db import models

# Create your models here.

class Ingredient(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name