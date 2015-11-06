class SearchRequestTestCaseMixin(object):

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
