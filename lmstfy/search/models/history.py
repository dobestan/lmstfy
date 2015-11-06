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

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = HistoryManager()

    class Meta:
        pass

    def __str__(self):
        return '"{query}" on {site_name} at {created_at}'.format(
            query=self.query.content,
            site_name=self.site.name,
            created_at=self.created_at,
        )

    def save(self, *args, **kwargs):
        super(History, self).save(*args, **kwargs)

        if not self.hash_id:
            self._create_hash_id()

    def get_absolute_url(self):
        # TODO: refactor using django.core.urlresolvers.reverse
        return "/%s/" % (self.hash_id, )

    def _create_hash_id(self):
        from search.utils.hash_id import get_encoded_hashid

        self.hash_id = get_encoded_hashid(self)
        self.save()
