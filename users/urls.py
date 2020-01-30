from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, profile

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register', UserRegisterView.as_view(template_name='users/register.html'), name='register'),
    path('profile', profile, name='profile')
]
