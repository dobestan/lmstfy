from django.contrib.sites.models import Site


class SearchRequestTestCaseMixin(object):

    def test_request(self):

        self.assertEqual(
            self.response.status_code,
            200,
        )

        self.assertContains(
            self.response,
            self.site.name,
        )
        self.assertContains(
            self.response,
            self.site.domain,
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
