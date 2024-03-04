from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# Create your models here.

class Comment(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_recipe = models.ForeignKey(Recipe, related_name="comments",on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.parent_recipe.title, self.author)