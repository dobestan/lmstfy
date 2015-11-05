from django.db import models


class QueryManager(models.Manager):
    pass


class Query(models.Model):

    content = models.CharField(
        max_length=255,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QueryManager()

    class Meta:
        pass

    def __str__(self):
        return self.content
