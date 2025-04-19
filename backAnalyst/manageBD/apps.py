import os
from django.apps import AppConfig


class ManagebdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manageBD'

    def ready(self):
         if os.environ.get('RUN_MAIN') == 'true':
            from backAnalyst.ready import start_mqtt
            start_mqtt()