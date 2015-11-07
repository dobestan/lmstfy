from django.core.urlresolvers import reverse

from .base import SearchBaseTestCase
from .mixins.test_request import SearchRequestTestCaseMixin
from search.models import Query, Result


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
