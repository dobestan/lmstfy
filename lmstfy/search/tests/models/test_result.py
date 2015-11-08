from django.test import TestCase
from django.contrib.sites.models import Site

from search.models import Query, Result
from search.utils.hash_id import get_encoded_hashid


class ResultManagerTestCase(TestCase):

    def setUp(self):
        self.site = Site.objects.create(
            name='test_site_name',
            domain='test_site_domain.com',
        )
        self.another_site = Site.objects.create(
            name='test_another_site_name',
            domain='test_another_site_domain.com',
        )

        self.test_query_content = 'test_query_content'
        self.query = Query.objects.create(
            content=self.test_query_content,
        )
        self.test_another_query_content = 'test_another_query_content'
        self.another_query = Query.objects.create(
            content=self.test_another_query_content,
        )

        self.result = Result.objects.create(
            site=self.site,
            query=self.query,
        )

    def test_get_or_none(self):
        """ResultManager should have get_or_none functionality."""

        self.assertEqual(
            Result.objects.get_or_none(
                site=self.site,
                query=self.query,
            ),
            self.result,
        )

        self.assertIsNone(
            Result.objects.get_or_none(
                site=self.another_site,
                query=self.query,
            ),
        )

        self.assertIsNone(
            Result.objects.get_or_none(
                site=self.site,
                query=self.another_query,
            ),
        )


class ResultTestCase(TestCase):

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

    def test_hash_id(self):
        """Result should have valid hash_id."""

        self.assertIsNotNone(self.result.hash_id)
        self.assertEqual(
            self.result.hash_id,
            get_encoded_hashid(self.result),
        )

        # Result should have valid hash_id on post_save "immediately".
        #
        # This test case will fails if create hash_id on post_save signal.
        # should override save method to create hash_id "immediately".
        self.assertIsNotNone(
            Result.objects.create(
                site=self.site,
                query=self.query,
            ).hash_id
        )

    def test_get_absolute_url(self):
        """Result should have absolute_url."""

        self.assertIsNotNone(
            self.result.get_absolute_url(),
        )

        # Result indicates unique histories(logs) instance for every search by user.
        # should have different absolute_url whether both result has same "site" and "query".
        self.assertNotEqual(
            self.result.get_absolute_url(),
            Result.objects.create(
                site=self.site,
                query=self.query,
            ).get_absolute_url(),
        )
