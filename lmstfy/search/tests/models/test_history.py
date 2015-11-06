from django.test import TestCase
from django.contrib.sites.models import Site

from search.models import Query, History
from search.utils.hash_id import get_encoded_hashid


class HistoryTestCase(TestCase):

    def setUp(self):
        self.site = Site.objects.create(
            name='test_site_name',
            domain='test_site_domain.com',
        )

        self.query = Query.objects.create(
            content='test_query',
        )

        self.history = History.objects.create(
            site=self.site,
            query=self.query,
        )

    def test_hash_id(self):
        """History should have valid hash_id."""

        self.assertIsNotNone(self.history.hash_id)
        self.assertEqual(
            self.history.hash_id,
            get_encoded_hashid(self.history),
        )

        # History should have valid hash_id on post_save "immediately".
        #
        # This test case will fails if create hash_id on post_save signal.
        # should override save method to create hash_id "immediately".
        self.assertIsNotNone(
            History.objects.create(
                site=self.site,
                query=self.query,
            ).hash_id
        )

    def test_get_absolute_url(self):
        """History should have absolute_url."""

        self.assertIsNotNone(
            self.history.get_absolute_url(),
        )

        # History indicates unique histories(logs) instance for every search by user.
        # should have different absolute_url whether both history has same "site" and "query".
        self.assertNotEqual(
            self.history.get_absolute_url(),
            History.objects.create(
                site=self.site,
                query=self.query,
            ).get_absolute_url(),
        )
