from django.shortcuts import render, reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


class UserRegisterView(CreateView):
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('login')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def home(request):
    return render(request, 'users/index.html')