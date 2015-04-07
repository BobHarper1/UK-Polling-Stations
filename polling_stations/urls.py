# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from polling_stations.api import router
from data_finder.views import HomeView, CouncilView, PostcodeView, CoverageView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^league_table', include('data_collection.urls')),
    url(r'^coverage$', CoverageView.as_view(), name='coverage'),

    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),

    url(r'^council/(?P<pk>.+)/$', CouncilView.as_view(), name='council'),
    url(r'^postcode/(?P<postcode>.+)/$',
        PostcodeView.as_view(), name='postcode_view'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

