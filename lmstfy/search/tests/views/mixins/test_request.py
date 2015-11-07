from django.contrib.sites.models import Site


class SearchRequestTestCaseMixin(object):

    def test_request(self):

        self.assertEqual(
            self.response.status_code,
            200,
        )

        self.assertEqual(
            self.response.context_data.get('current_site'),
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

        self.assertIsNotNone(
            self.response.context_data.get('sites', None),
        )
        self.assertEqual(
            list(self.response.context_data.get('sites', None)),
            list(Site.objects.all()),
        )

        for site in Site.objects.all():
            self.assertContains(
                self.response,
                site.name,
            )
            self.assertContains(
                self.response,
                site.domain,
            )
