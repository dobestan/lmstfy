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
