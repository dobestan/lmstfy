from django.test import TestCase
from django.contrib.sites.models import Site
from django.test.client import Client
from django.core.urlresolvers import reverse


class MultisitesContextProcessorsTestCase(TestCase):

    def setUp(self):
        # If context is added via get_context_data method,
        # context is accessible from response "context_data".
        #
        # On the other hand, if context is added via context_processors,
        # context is accessible from response "context".

        self.site = Site.objects.create(
            name='testserver',
            domain='testserver',
        )
        Site.objects.clear_cache()
        self.client = Client()
        self.response = self.client.get(reverse('search:home'))

    def test_current_site(self):
        """RequestContext should have valid current_site information."""

        self.assertEqual(
            self.response.context.get('current_site'),
            self.site,
        )

    def test_sites(self):
        """RequestContext should have valid sites information."""
        self.assertIsNotNone(
            self.response.context.get('sites', None),
        )
        self.assertEqual(
            list(self.response.context.get('sites', None)),
            list(Site.objects.all()),
        )
