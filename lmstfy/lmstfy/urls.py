from django.conf.urls import include, url
from django.contrib import admin

from lmstfy.views import Home


urlpatterns = [
    url(r'^lmstfy/', include(admin.site.urls)),

    url(r'^$', Home.as_view(), name='home'),
]
