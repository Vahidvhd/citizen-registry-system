from django.contrib.auth.models import User
from django.test import TestCase

from .models import UsageProfile


class UsageProfileModelTest(TestCase):
    def test_usage_profile_string_representation(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = user.usageprofile

        self.assertEqual(
            str(profile),
            'vahid usage profile'
        )

    def test_usage_profile_default_limits(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = user.usageprofile

        self.assertEqual(profile.daily_limit, 10)
        self.assertEqual(profile.monthly_limit, 100)
        self.assertEqual(profile.daily_used, 0)
        self.assertEqual(profile.monthly_used, 0)

    def test_user_can_search_when_under_limit(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = user.usageprofile

        self.assertTrue(profile.can_search())

    def test_consume_token_increases_usage(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = user.usageprofile
        profile.consume_token()

        self.assertEqual(profile.daily_used, 1)
        self.assertEqual(profile.monthly_used, 1)

    def test_user_cannot_search_when_daily_limit_is_reached(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = user.usageprofile
        profile.daily_used = 10
        profile.save()

        self.assertFalse(profile.can_search())

    def test_daily_remaining_returns_available_daily_tokens(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = user.usageprofile
        profile.daily_limit = 10
        profile.daily_used = 4
        profile.save()

        self.assertEqual(profile.daily_remaining(), 6)

    def test_monthly_remaining_returns_available_monthly_tokens(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = user.usageprofile
        profile.monthly_limit = 100
        profile.monthly_used = 25
        profile.save()

        self.assertEqual(profile.monthly_remaining(), 75)

    def test_usage_profile_is_created_when_user_is_created(self):
        user = User.objects.create_user(
            username='operator_auto',
            password='StrongPass123!',
        )

        self.assertTrue(
            UsageProfile.objects.filter(user=user).exists()
        )