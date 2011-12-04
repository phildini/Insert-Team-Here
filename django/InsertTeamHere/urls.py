from django.conf.urls.defaults import patterns, include, url 
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'InsertTeamHere.views.home', name='home'),
    # url(r'^InsertTeamHere/', include('InsertTeamHere.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
<<<<<<< HEAD
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.backends.default.urls')),
=======
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('registration.urls')),
>>>>>>> d32c24d50e13941f3c6963e96e2b33fd8863310a

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),

    #Team App URLs
    url(r'^teams/', include('teams.urls')),
)
