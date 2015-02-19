from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taskboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'website.views.index'),
    url(r'^profile/$', 'website.views.profile'),
    url(r'^post/$', 'website.views.index'),
    url(r'^feed/$', 'website.views.index'),

    url(r'^ajax/register/$', 'website.views.ajax_register'),
)
