from django.test import LiveServerTestCase
from django.contrib.sites.models import Site

from selenium import webdriver

from functional_tests.utils.selenium import get_selenium_driver


class APITestCase(LiveServerTestCase):

    def setUp(self):
        self.driver = get_selenium_driver()

        # FIXME: Should refactor creating a site with live_server_url.
        #
        # By Default,
        #   self.live_server_url returns "http://localhost:8081"
        #   self.site.domain should be "localhost:8081"
        #
        # Create a site instance with self.live_server_url, not by raw url string "localhost:8081".
        self.site = Site.objects.create(
            name='live_server_name',
            domain='localhost:8081',
        )

    def tearDown(self):
        self.driver.quit()

    def test_api_docs(self):
        """API Documentation."""

        self.driver.get('%s%s' % (
            self.live_server_url,
            '/api/docs/',
        ))

        self.assertEqual(
            '%s API Docs' % (self.site.name, ),
            self.driver.title,
        )
