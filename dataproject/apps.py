from django.apps import AppConfig
from django.conf import settings

print(settings.TEMPLATES)


class DataprojectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dataproject'
