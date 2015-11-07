from django.views.generic.detail import DetailView

from .base import SearchBaseView
from search.models import Result


class SearchResultView(SearchBaseView, DetailView):
    model = Result
    slug_field = 'hash_id'
    context_object_name = 'result'
