from django.apps import AppConfig


class AppartementmanagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ApartmentManager'

    def ready(self):
        import ApartmentManager.signals
        return super().ready()
