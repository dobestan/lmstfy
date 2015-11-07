from django.test import TestCase
from django.contrib.sites.models import Site

from search.models import Query, Result, History


class HistoryTestCase(TestCase):

    def setUp(self):
        self.site = Site.objects.create(
            name='test_site_name',
            domain='test_site_domain.com',
        )

        self.query = Query.objects.create(
            content='test_query',
        )

        self.result = Result.objects.create(
            site=self.site,
            query=self.query,
        )

        # Create history instance without site, query information.
        # History save site, query information via result instance.
        self.history = History.objects.create(
            result=self.result,
        )

    def test_site(self):
        """History should have valid site."""

        self.assertIsNotNone(
            self.history.site,
        )
        self.assertEqual(
            self.history.site,
            self.site,
        )

    def test_query(self):
        """History should have valid query."""

        self.assertIsNotNone(
            self.history.query,
        )
        self.assertEqual(
            self.history.query,
            self.query,
        )
