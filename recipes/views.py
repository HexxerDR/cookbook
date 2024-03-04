from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django import forms

from . import models
# Create your views here.

class RecipeIngredientForm(forms.Form):
    ingredient_to_add= forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    amount_choices = {1 : "Liquid (milliliters)", 2 : "Liquid (liters)" , 3 : "Amount", 4 : "Weight (grams)", 5 : "Weight (kilograms)"}
    amount_type = forms.ChoiceField(widget=forms.Select(), choices = amount_choices)
    amount = forms.DecimalField(max_digits=6, decimal_places=2)

class RecipeRemoveIngredientForm(forms.Form):
    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        recipe = get_object_or_404(models.Recipe, pk=id)
        recipeing = recipe.ingredients_list
        self.fields['ing_delete'] = forms.ChoiceField(choices = recipeing, widget=forms.Select())

class RecipeListView(ListView):
    model = models.Recipe
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = models.Recipe

class RecipeCreateView(LoginRequiredMixin, CreateView, RecipeIngredientForm):
    model = models.Recipe
    fields = ['title', 'description']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author or self.request.user.is_staff

class RecipeAddIngredient(LoginRequiredMixin, UserPassesTestMixin, FormView):
    model = models.Recipe
    form_class = RecipeIngredientForm
    
    template_name = "recipes/recipe_ing_add.html"

    def test_func(self):
        pk = self.kwargs['pk']
        recipe = get_object_or_404(models.Recipe, pk=pk)
        return self.request.user == recipe.author
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        recipe = get_object_or_404(models.Recipe, pk=pk)
        types = ["none", "ml", "l", "x", "g", "kg"]
        typeint = int(form.cleaned_data["amount_type"])
        if typeint == 3:
            ingredient_to_add = str(form.cleaned_data['ingredient_to_add']) + " " +str(form.cleaned_data['amount']) + str(types[typeint])
        else:
            ingredient_to_add = str(form.cleaned_data['ingredient_to_add']) + " " +str(form.cleaned_data['amount']) + " " + str(types[typeint])
        k = str(len(recipe.ingredients_list) + 1)
        key = "ing"+k
        recipe.ingredients_list[key] = ingredient_to_add
        recipe.ingredients_price_list[key] = float(form.cleaned_data['price'])
        recipe.price_total = sum(list(recipe.ingredients_price_list.values()))
        recipe.save()
        return super().form_valid(form)
        
    success_url = reverse_lazy('recipes-home')

class RecipeRemoveIngredient(LoginRequiredMixin, UserPassesTestMixin, FormView):
    model = models.Recipe
    form_class = RecipeRemoveIngredientForm

    template_name = "recipes/recipe_ing_remove.html"

    def test_func(self):
        pk = self.kwargs['pk']
        recipe = get_object_or_404(models.Recipe, pk=pk)
        return self.request.user == recipe.author
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["id"] = self.kwargs["pk"]
        return kwargs

    def form_valid(self, form):
        id = self.kwargs['pk']
        recipe = get_object_or_404(models.Recipe, pk=id)
        recipe.ingredients_list.pop(str(form.cleaned_data['ing_delete']))
        recipe.ingredients_price_list.pop(str(form.cleaned_data['ing_delete']))
        recipe.price_total = sum(list(recipe.ingredients_price_list.values()))
        recipe.save()
        return super().form_valid(form)
        
    success_url = reverse_lazy('recipes-home')

def about(request):
    return render(request, "recipes/about.html", {'title': 'About page'})

