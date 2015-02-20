from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taskboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'website.views.index'),
    url(r'^profile/$', 'website.views.profile'),
    url(r'^post/$', 'website.views.post'),
    url(r'^feed/$', 'website.views.feed'),

    url(r'^commission/$', 'website.views.commission'),
    url(r'^commission/change/$', 'website.views.commission_change'),

    url(r'^ajax/register/$', 'website.views.ajax_register'),
    url(r'^ajax/login/$', 'website.views.ajax_login'),
    url(r'^ajax/logout/$', 'website.views.ajax_logout'),
    url(r'^ajax/post/$', 'website.views.ajax_post_task'),
    url(r'^ajax/take/(\d+)/$', 'website.views.ajax_take_task'),

    url(r'^$', 'django.contrib.auth.views.login'),
)
