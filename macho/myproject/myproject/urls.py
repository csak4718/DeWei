from django.conf.urls import patterns, include, url

from django.contrib import admin
import dwkung.views
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'myproject.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^dwkung/',include('dwkung.urls')),
	url(r'^polls/', include('polls.urls', namespace="polls")), 
	url(r'^admin/', include(admin.site.urls)),
)
