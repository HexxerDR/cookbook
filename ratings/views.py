from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from . import models
from comments.models import Comment
from recipes.models import Recipe
# Create your views here.

@login_required()
def RecipeRating(request, pk):
    recipe = Recipe.objects.get(id=pk)
    user = request.user
    current_likes = recipe.rating_total
    liked = models.Rating.objects.filter(rating_user=user, rated_recipe=recipe)
    if not liked:
        liked = models.Rating.objects.create(rating_user=user, rated_recipe=recipe)
        current_likes += 1
    else:
       liked = models.Rating.objects.filter(rating_user=user, rated_recipe=recipe).delete()
       current_likes -= 1
    recipe.rating_total = current_likes
    recipe.save()

    return HttpResponseRedirect(reverse('recipes-detail', args=[pk]))