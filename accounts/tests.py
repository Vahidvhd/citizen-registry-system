from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class SignupViewTest(TestCase):
    def test_signup_page_returns_200(self):
        response = self.client.get(reverse('signup'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_user_can_signup_with_valid_data(self):
        response = self.client.post(
            reverse('signup'),
            data={
                'username': 'vahid',
                'password1': 'Testpassword!',
                'password2': 'Testpassword!',
            }
        )

        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, reverse('login'))


class LoginViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='vahid',
            password='Testpassword!',
        )

    def test_login_page_returns_200(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_user_can_login_with_valid_credentials(self):
        response = self.client.post(
            reverse('login'),
            data={
                'username': 'vahid',
                'password': 'Testpassword!',
            }
        )

        self.assertRedirects(response, reverse('search'))