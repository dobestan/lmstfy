from django.core.urlresolvers import reverse

from .base import SearchBaseTestCase
from .mixins.test_request import SearchRequestTestCaseMixin


class SearchHomeViewTestCase(SearchBaseTestCase, SearchRequestTestCaseMixin):

    def setUp(self):
        super(SearchHomeViewTestCase, self).setUp()

        self.response = self.client.get(reverse('search:home'))
