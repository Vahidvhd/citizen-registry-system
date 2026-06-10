from django.db import models
from django.conf import settings

# Create your models here.
class UsageProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    daily_limit = models.PositiveIntegerField(default=10)
    monthly_limit = models.PositiveIntegerField(default=100)
    daily_used = models.PositiveIntegerField(default=0)
    monthly_used = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} usage profile'