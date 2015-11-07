from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site


def sites(request):
    """Returns context variables related to djagno site framework."""

    return {
        'current_site': get_current_site(request),
        'sites': Site.objects.all(),
    }
