from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#from ingredients.models import Ingredient
# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_total = models.BigIntegerField(default = 0)
    ingredients_list = models.JSONField(default=dict)
    ingredients_price_list = models.JSONField(default=dict)
    price_total = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)


    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title