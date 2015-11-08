from django.contrib.sites.shortcuts import get_current_site
from django.views.generic.detail import DetailView

from .base import SearchBaseView
from search.models import Result, History


class SearchResultView(SearchBaseView, DetailView):
    model = Result
    slug_field = 'hash_id'
    context_object_name = 'result'

    def dispatch(self, *args, **kwargs):

        # Create History instance on request.
        History.objects.create(
            result=self.get_object(),
        )

        return super(SearchResultView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        """SearchResultView queryset should return results only in current_site."""

        queryset = super(SearchResultView, self).get_queryset()

        current_site = get_current_site(self.request)
        return queryset.filter(
            site=current_site,
        )
