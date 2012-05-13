from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'family.album.views.all', name = 'album_all'),
    url(r'^family/$', 'family.album.views.family', name = 'album_family'),
    url(r'^trash/$', 'family.album.views.trash', name = 'album_trash'),
    url(r'^mines/$', 'family.album.views.mines', name = 'album_mines'),
    url(r'^(?P<album_id>\d+)$', 'family.album.views.detail', name = 'album_detail'),
)