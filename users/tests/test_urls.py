from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LoginView
from users.views import UserRegisterView, profile


class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, UserRegisterView)

    def test_profile_url(self):
        url = reverse('profile')
        print('resolved:', resolve(url).func)
        self.assertEquals(resolve(url).func, profile)
