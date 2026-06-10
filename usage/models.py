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
    
    def can_search(self):
        return (
            self.daily_used < self.daily_limit
            and self.monthly_used < self.monthly_limit
        )

    def consume_token(self):
        if not self.can_search():
            return False

        self.daily_used += 1
        self.monthly_used += 1
        self.save(update_fields=['daily_used', 'monthly_used'])

        return True
    
    def daily_remaining(self):
        return self.daily_limit - self.daily_used

    def monthly_remaining(self):
        return self.monthly_limit - self.monthly_used