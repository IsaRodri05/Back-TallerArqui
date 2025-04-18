from django.apps import AppConfig


class ManagebdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manageBD'

    def ready(self):
        from backAnalyst.ready import start_mqtt
        start_mqtt()