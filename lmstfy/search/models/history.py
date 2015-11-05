from django.db import models
from django.contrib.sites.models import Site

from search.models import Query


class HistoryManager(models.Manager):
    pass


class History(models.Model):

    site = models.ForeignKey(
        Site,
    )

    query = models.ForeignKey(
        Query,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = HistoryManager()

    class Meta:
        pass
