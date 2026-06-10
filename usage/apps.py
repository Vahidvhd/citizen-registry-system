from django.apps import AppConfig


class UsageConfig(AppConfig):
    name = 'usage'

    def ready(self):
        import usage.signals