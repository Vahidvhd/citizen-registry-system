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


    def test_user_can_search_when_under_limit(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = UsageProfile.objects.create(
            user=user,
        )

        self.assertTrue(profile.can_search())


    def test_consume_token_increases_usage(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = UsageProfile.objects.create(
            user=user,
        )

        profile.consume_token()

        self.assertEqual(profile.daily_used, 1)
        self.assertEqual(profile.monthly_used, 1)


    def test_user_cannot_search_when_daily_limit_is_reached(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = UsageProfile.objects.create(
            user=user,
            daily_used=10,
        )

        self.assertFalse(profile.can_search())


    def test_daily_remaining_returns_available_daily_tokens(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = UsageProfile.objects.create(
            user=user,
            daily_limit=10,
            daily_used=4,
        )

        self.assertEqual(profile.daily_remaining(), 6)


    def test_monthly_remaining_returns_available_monthly_tokens(self):
        user = User.objects.create_user(
            username='vahid',
            password='Vahidtest!',
        )

        profile = UsageProfile.objects.create(
            user=user,
            monthly_limit=100,
            monthly_used=25,
        )

        self.assertEqual(profile.monthly_remaining(), 75)