from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from family.models import Album, Photo
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required()
@user_passes_test(lambda u: u.is_superuser)
def all(request):
    albums = Album.objects.all().order_by('name')

    return render_to_response(
        'family/album/all.html',
        { 'albums': albums },
        RequestContext(request),
    )

@login_required()
@user_passes_test(lambda u: u.groups.filter(name='family').count() != 0 or u.is_superuser)
def family(request):
    albums = Album.objects.filter(public = True).order_by('name')

    return render_to_response(
        'family/album/family.html',
        {'albums': albums},
        RequestContext(request),
    )

@login_required()
def mines(request):
    albums = request.user.album_set.all()
    return render_to_response(
        'family/album/mines.html',
        {'albums': albums},
        RequestContext(request),
    )

@login_required()
def detail(request, album_id):
    photos = Album.objects.get(pk = album_id).photo_set.all()
    return render_to_response(
        'family/album/detail.html',
        {'photos': photos},
        RequestContext(request),
    )

@login_required()
@user_passes_test(lambda u: u.is_superuser)
def trash(request):
    photos = Photo.objects.filter(album = None)
    return render_to_response(
        'family/album/trash.html',
        {'photos': photos},
        RequestContext(request),
    )
