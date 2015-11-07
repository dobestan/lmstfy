from django.conf.urls import include, url
from django.contrib import admin

from search.views import SearchHomeView, SearchResultView


urlpatterns = [
    url(r'^lmstfy/', include(admin.site.urls)),

    url(r'^', include([
        url(r'^$', SearchHomeView.as_view(), name='home'),
        url(r'^(?P<slug>\w+)/$', SearchResultView.as_view(), name='result'),
    ], namespace='search', app_name='search')),
]
