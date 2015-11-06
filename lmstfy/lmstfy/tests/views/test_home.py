from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class HomeViewTestCase(TestCase):

    def setUp(self):

        # "testserver" is reserved keyword for default test server name, domain.
        self.site = Site.objects.create(
            name='testserver',
            domain='testserver',
        )

        self.client = Client()
        self.response = self.client.get(reverse('home'))

    def test_request(self):

        self.assertEqual(
            self.response.status_code,
            200,
        )

        self.assertEqual(
            self.response.context_data.get('site'),
            self.site,
        )

        self.assertContains(
            self.response,
            self.site.name,
        )
        self.assertContains(
            self.response,
            self.site.domain,
        )
