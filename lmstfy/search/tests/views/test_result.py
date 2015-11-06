from django.core.urlresolvers import reverse

from .base import SearchBaseTestCase
from .mixins.test_request import SearchRequestTestCaseMixin


class SearchResultViewTestCase(SearchBaseTestCase, SearchRequestTestCaseMixin):

    def setUp(self):
        super(SearchResultViewTestCase, self).setUp()

        self.response = self.client.get(
            reverse('search:result', kwargs={'hash_id': 'hash_id'})
        )
