from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ajax_select import urls as ajax_select_urls
admin.autodiscover()

urlpatterns = patterns('',
    # include the lookup urls
    (r'^admin/lookups/', include(ajax_select_urls)),

    # Examples:
    # url(r'^$', 'collection_registry.views.home', name='home'),
    url(r'^collection_registry/', include('dl_collections.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
