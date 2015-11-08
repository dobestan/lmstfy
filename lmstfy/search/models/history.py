from django.db import models
from django.contrib.sites.models import Site

from search.models import Query, Result


class HistoryManager(models.Manager):
    pass


class History(models.Model):

    site = models.ForeignKey(
        Site,
    )

    query = models.ForeignKey(
        Query,
    )

    result = models.ForeignKey(
        Result,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    objects = HistoryManager()

    class Meta:
        get_latest_by = 'created_at'
        ordering = [
            '-created_at',
        ]

    def __str__(self):
        return '"{query}" on {site_name} visited at {created_at}'.format(
            query=self.query.content,
            site_name=self.site.name,
            created_at=self.created_at,
        )
