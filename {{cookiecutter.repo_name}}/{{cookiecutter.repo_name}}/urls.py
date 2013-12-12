# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

class HomePageView(TemplateView):
    template_name = "homepage.html"

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r"^$",
        HomePageView.as_view(),
        name="home"),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)