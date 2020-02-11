from django.test import TestCase
from users.forms import RegisterForm


class TestRegisterForm(TestCase):

    def test_correct_form_validation(self):
        form = RegisterForm(data={
            'username': 'User1',
            'email': 'user1@email.com',
            'password1': 'veryStrongPassWord',
            'password2': 'veryStrongPassWord'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_email_validation(self):
        form = RegisterForm(data={
            'username': 'User1',
            'email': '32&8/.com',
            'password1': 'veryStrongPassWord',
            'password2': 'veryStrongPassWord'
        })
        print('email errors:', form.errors)
        self.assertEquals(form.errors['email'], ['Enter a valid email address.'])

    def test_weak_password_validation(self):
        form = RegisterForm(data={
            'username': 'User1',
            'email': 'user1@email.com',
            'password1': '1',
            'password2': '1'
        })
        self.assertEquals(form.errors['password2'], ['This password is too short. It must contain at least 8 characters.',
                                                     'This password is too common.',
                                                     'This password is entirely numeric.'])
