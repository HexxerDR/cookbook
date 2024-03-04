from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import views as auth_views

from . import forms

# Create your vie
# ws here.

def register(request):
    user = request.user
    if not user.is_authenticated:
        if request.method == "POST":
            form = forms.UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"{username}, your account has been created!")
                return redirect('user-login')
        else:
            form = forms.UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    else:
        return redirect('recipes-home')


class CustomLogin(UserPassesTestMixin, auth_views.LoginView):
    model = User

    def test_func(self):
        return not self.request.user.is_authenticated
    
class CustomLogout(LoginRequiredMixin, auth_views.LogoutView):
    model = User

    

@login_required()
def profile(request):
    return render(request, "users/profile.html")