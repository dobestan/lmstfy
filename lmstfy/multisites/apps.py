from django.apps import AppConfig


class MultisitesAppConfig(AppConfig):
    name = 'multisites'

    def ready(self):
        from multisites.signals.post_save import post_save_site
