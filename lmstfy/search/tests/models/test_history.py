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

    def test_order(self):
        """History should order in created_at DESC order."""

        from random import randint

        history_list = list()
        history_counts = randint(1, 100)

        history_list.append(self.history)

        for i in range(1, history_counts + 1):
            history = History.objects.create(
                result=self.result,
            )
            history_list.append(history)

        self.assertEqual(
            History.objects.latest(),
            history,
        )

        history_list.reverse()
        self.assertEqual(
            list(History.objects.all()),
            history_list,
        )
