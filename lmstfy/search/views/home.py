from django.views.generic import TemplateView

from .base import SearchBaseView


class SearchHomeView(SearchBaseView, TemplateView):
    pass
