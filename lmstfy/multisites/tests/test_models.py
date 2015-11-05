from django.test import TestCase
from django.contrib.sites.models import Site

from multisites.models import SiteProfile


class SiteProfileTestCase(TestCase):

    def setUp(self):
        self.site = Site.objects.create(
            name='test_site_name',
            domain='test_site_domain.com',
        )

        self.test_search_query = "test_search_query"

    def test_site_profile_created(self):
        """SiteProfile should be created on post save Site."""

        self.site.site_profile

        self.assertEqual(
            Site.objects.count(),
            SiteProfile.objects.count(),
        )

    def test_site_profile_provider_search_url(self):
        """SiteProfile has ability to generate search_result_url with query."""

        self.site.site_profile.provider_search_url = "http://search.naver.com/search.naver?query={query}"
        self.site.site_profile.save()

        self.assertEqual(
            self.site.site_profile.get_search_result_url(self.test_search_query),
            "http://search.naver.com/search.naver?query=test_search_query",
        )
