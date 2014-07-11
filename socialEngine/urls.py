from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'socialApp.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'socialApp.views.register'),
    url(r'^login/', 'socialApp.views.login'),
    url(r'^follows/', 'socialApp.views.follows'),


)
