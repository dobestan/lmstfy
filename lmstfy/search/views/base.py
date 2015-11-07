from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site


class SearchBaseView(DetailView):
    template_name = "base.html"
    context_object_name = 'current_site'

    def get_object(self):
        return get_current_site(self.request)

    def get_context_data(self, *args, **kwargs):
        context = super(SearchBaseView, self).get_context_data(**kwargs)

        context['sites'] = Site.objects.all()

        return context
