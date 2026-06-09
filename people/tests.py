from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Citizen


class PeopleAppSmokeTest(TestCase):
    def test_people_app_is_working(self):
        self.assertTrue(True)

class CitizenModelTest(TestCase):
    def test_citizen_string(self):
        citizen = Citizen.objects.create(
            first_name='vahid',
            last_name='vahedi',
            national_code='1234567890',
            date_of_birth='1991-01-01',
            phone_number='+989121111111',
            email='vahid@test.com',
            address='London',
        )
        self.assertEqual(str(citizen), 'vahid vahedi - 1234567890')


class SearchViewAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='operator1',
            password='StrongPass123!',
        )

    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.get(reverse('search'))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('search')}"
        )

    def test_authenticated_user_can_access_search_page(self):
        self.client.login(
            username='operator1',
            password='StrongPass123!',
        )

        response = self.client.get(reverse('search'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'people/search.html')