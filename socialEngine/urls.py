from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin:
    url(r'^admin/$', include(admin.site.urls)),
    # User:
    url(r'^$', 'socialApp.views.home'),
    url(r'^register/$', 'socialApp.views.register'),
    url(r'^login/$', 'socialApp.views.login'),
    url(r'^error_login/$', 'socialApp.views.error_login'),
    url(r'^logout/$', 'socialApp.views.logout'),
    url(r'^follows/$', 'socialApp.views.follows'),


)
