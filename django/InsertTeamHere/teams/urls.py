from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('teams.views',
	url(r'^$', 'index'),
	url(r'^(?P<team_id>\d+)/$', 'detail'),
	url(r'^(?P<team_id>\d+)/edit/$', 'edit'),
	url(r'^add/$', 'add'),
)
