from django.contrib.sites.models import Site
from django.test import TestCase
from django.test.client import Client


class SearchBaseTestCase(TestCase):

    def setUp(self):

        # "testserver" is reserved keyword for default test server name, domain.
        self.site = Site.objects.create(
            name='testserver',
            domain='testserver',
        )

        # Django caches the current Site object.
        # Explicitly clear cache to prevent from potential errors on test.
        Site.objects.clear_cache()

        self.client = Client()
