from django.conf.urls import url, patterns, include

urlpatterns = patterns('',
    url(r'^album/', include('family.album.urls')),
)