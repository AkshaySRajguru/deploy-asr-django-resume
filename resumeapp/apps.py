from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resumeapp'
    def ready(self):
        import resumeapp.signals
