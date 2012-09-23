from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dl_collections.views.home', name='home'),
    # Status/Format/Restriction/Need
    url(r'^(UC.*)$', 'dl_collections.views.UC', name='UC'),
    #url(r'^(UC.*)/(Status)/(.*)$', 'dl_collections.views.UClimit', name='UClimit'),
    #url(r'^(UC.*)/(Format)/(.*)$', 'dl_collections.views.UClimit', name='UClimit'),
    #url(r'^(UC.*)/(Restriction)/(.*)$', 'dl_collections.views.UClimit', name='UClimit'),
    #url(r'^(UC.*)/(Need)/(.*)$', 'dl_collections.views.UClimit', name='UClimit'),
    #url(r'^(?P<slug>.*)$', 'dl_collections.views.details', name='detail'),
    url(r'^(.*)$', 'dl_collections.views.details', name='detail'),
)
