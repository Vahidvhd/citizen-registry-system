from django.contrib.auth.models import User
from django.test import TestCase
from .models import UsageProfile


class UsageProfileModelTest(TestCase):
    def test_usage_profile_string_representation(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = UsageProfile.objects.create(
            user=user,
        )

        self.assertEqual(
            str(profile),
            'vahid usage profile'
        )

    def test_usage_profile_default_limits(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = UsageProfile.objects.create(
            user=user,
        )

        self.assertEqual(profile.daily_limit, 10)
        self.assertEqual(profile.monthly_limit, 100)
        self.assertEqual(profile.daily_used, 0)
        self.assertEqual(profile.monthly_used, 0)