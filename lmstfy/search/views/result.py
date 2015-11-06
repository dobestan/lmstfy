from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site


class SearchResultView(DetailView):
    template_name = "base.html"
    context_object_name = 'site'

    def get_object(self):
        return get_current_site(self.request)
