from django.test import TestCase
from django.contrib.sites.models import Site

from multisites.models import SiteProfile


class SiteProfileTestCase(TestCase):

    def setUp(self):
        self.site = Site.objects.create(
            name='test_site_name',
            domain='test_site_domain.com',
        )

    def test_site_profile_created(self):
        """SiteProfile should be created on post save Site."""

        self.site.site_profile

        self.assertEqual(
            Site.objects.count(),
            SiteProfile.objects.count(),
        )
