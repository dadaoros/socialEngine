from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Admin:
    url(r'^admin/', include(admin.site.urls)),
    # User:
    url(r'^$', 'socialApp.views.home'),
    url(r'^login/$', 'socialApp.views.log_in'),
    url(r'^login/auth/$', 'socialApp.views.auth_view'),
    url(r'^error_login/$', 'socialApp.views.error_login'),
    url(r'^logout/$', 'socialApp.views.log_out'),
    url(r'^follows/$', 'socialApp.views.follows'),
    url(r'^register/$', 'socialApp.views.register_user'),
    url(r'^register_success/$', 'socialApp.views.register_success'),
    url(r'^profile/(\d{1,5})/$', 'socialApp.views.wall'),
    url(r'^profile/$', 'socialApp.views.show_profiles'),

)
