from django.db import models
from django.contrib.auth.models import User

from recipes.models import Recipe

class Rating(models.Model):
    rated_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating_user = models.ForeignKey(User, on_delete=models.CASCADE)