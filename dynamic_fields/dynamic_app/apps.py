from django.apps import AppConfig


class DynamicAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dynamic_app'
