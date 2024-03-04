from django.urls import path
from . import views

urlpatterns = [
    path('recipe/<int:pk>/like', views.RecipeRating, name='recipes-like')
]