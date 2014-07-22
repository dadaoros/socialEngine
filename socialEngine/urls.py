from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin:
    url(r'^admin/', include(admin.site.urls)),
    # User:
    url(r'^$', 'socialApp.views.home'),
    url(r'^register/$', 'socialApp.views.register'),
    url(r'^login/$', 'socialApp.views.log_in'),
    url(r'^login/auth/$', 'socialApp.views.auth_view'),
    url(r'^error_login/$', 'socialApp.views.error_login'),
    url(r'^logout/$', 'socialApp.views.log_out'),
    url(r'^follows/$', 'socialApp.views.follows'),


)
