from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes-home'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipes-create'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipes-detail'),
    path('recipe/<int:pk>/addi', views.RecipeAddIngredient.as_view(), name='recipes-ingredient'),
    path('recipe/<int:pk>/remi', views.RecipeRemoveIngredient.as_view(), name='recipes-ingredientremove'),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipes-update'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipes-delete'),
]
