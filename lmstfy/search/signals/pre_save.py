from django.db.models.signals import pre_save
from django.dispatch import receiver

from search.models import History


@receiver(pre_save, sender=History)
def pre_save_history(sender, instance, **kwargs):
    instance.site = instance.result.site
    instance.query = instance.result.query
