from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.models import Site

from multisites.models import SiteProfile


@receiver(post_save, sender=Site)
def post_save_site(sender, instance, created, **kwargs):
    if created:
        SiteProfile.objects.create(
            site=instance,
        )
