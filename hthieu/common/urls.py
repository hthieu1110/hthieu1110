from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/', 'common.views.login', name = 'common_login'),
    url(r'^logout/', 'common.views.logout', name = 'common_logout'),
    url(r'^delete/$', 'common.views.delete', name = 'common_delete'),
    url(r'empty_trash/$', 'common.views.empty_trash', name = 'common_empty_trash'),
)