from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from . import models
from recipes.models import Recipe
# Create your views here.


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Ingredient
    fields = ['price', 'name']

    def form_valid(self, form):
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('recipes-detail', kwargs={'pk': self.kwargs['pk']})