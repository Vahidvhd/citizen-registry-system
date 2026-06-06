from django.test import TestCase
from .models import Citizen

# Create your tests here.
class PeopleAppSmokeTest(TestCase):
    def test_peaople_app_is_working(self):
        self.assertTrue(True)

class CitizenModelTest(TestCase):
    def test_citizen_string(self):
        citizen= Citizen.objects.create(
            first_name ='vahid',
            last_name='vahedi',
            national_code='1234567890',
            date_of_birth='1991-01-01',
            phone_number='07415678901',
            email='vahid@test.com',
            address='London',
        )
        self.assertEqual(str(citizen), 'vahid vahedi - 1234567890')

