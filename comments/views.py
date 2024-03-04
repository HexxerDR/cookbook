from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from . import models
from recipes.models import Recipe
# Create your views here.


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    fields = ['description']

    def form_valid(self, form):
        form.instance.parent_recipe_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('recipes-detail', kwargs={'pk': self.kwargs['pk']})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Comment
    fields = ['description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipes-detail', kwargs={'pk': self.kwargs['post_pk']})
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Comment

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_staff
    
    def get_success_url(self):
        return reverse_lazy('recipes-detail', kwargs={'pk': self.kwargs['post_pk']})