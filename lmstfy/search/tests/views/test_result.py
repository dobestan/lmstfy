from django.core.urlresolvers import reverse

from .base import SearchBaseTestCase
from .mixins.test_request import SearchRequestTestCaseMixin
from search.models import Query, Result, History


class SearchResultViewTestCase(SearchBaseTestCase, SearchRequestTestCaseMixin):

    def setUp(self):
        super(SearchResultViewTestCase, self).setUp()

        self.query = Query.objects.create(
            content='test_query',
        )

        self.result = Result.objects.create(
            site=self.site,
            query=self.query,
        )

        self.response = self.client.get(
            reverse('search:result', kwargs={'slug': self.result.hash_id})
        )

    def test_result(self):
        """SearchResultView should have valid Result."""

        self.assertIsNotNone(
            self.response.context_data.get('result'),
        )
        self.assertEqual(
            self.response.context_data.get('result'),
            self.result,
        )

        self.assertContains(
            self.response,
            self.query.content,
        )

    def test_history(self):
        """History instance should be created on request on SearchResultView."""

        from random import randint

        # New Request on SearchResultView
        current_history_count = History.objects.count()
        self.client.get(
            reverse('search:result', kwargs={'slug': self.result.hash_id})
        )

        self.assertEqual(
            current_history_count + 1,
            History.objects.count(),
        )

        # New Random Count Requests on SearchResultView
        current_history_count = History.objects.count()
        request_counts = randint(1, 100)

        for i in range(1, request_counts + 1):
            self.client.get(
                reverse('search:result', kwargs={'slug': self.result.hash_id})
            )
            self.assertEqual(
                current_history_count + i,
                History.objects.count(),
            )
