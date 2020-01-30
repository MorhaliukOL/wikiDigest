from django.shortcuts import render, reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class UserRegisterView(CreateView):
    model = User
    fields = ['username', 'email', 'password']

    def get_success_url(self):
        return reverse('login')


@login_required
def profile(request):
    return render(request, 'users/profile.html')
