from django.db import models
from django.contrib.sites.models import Site


class SiteProfileManager(models.Manager):
    pass


class SiteProfile(models.Model):

    site = models.OneToOneField(
        Site,
        primary_key=True,
    )

    objects = SiteProfileManager()

    class Meta:
        db_table = 'multisites_site_profile'
        default_related_name = 'site_profile'

    def __str__(self):
        return self.site.__str__()
