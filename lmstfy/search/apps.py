from django.apps import AppConfig


class SearchAppConfig(AppConfig):
    name = 'search'

    def ready(self):
        from search.signals.pre_save import pre_save_history
