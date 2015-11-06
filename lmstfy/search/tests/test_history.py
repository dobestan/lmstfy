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

    def test_history_hash_id(self):
        """History should have valid hash_id."""

        history = History.objects.create(
            site=self.site,
            query=self.query,
        )

        self.assertIsNotNone(history.hash_id)
        self.assertEqual(
            history.hash_id,
            get_encoded_hashid(history),
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
