from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.views.decorators.cache import never_cache
from common.forms import CommonLoginForm
from common.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
from django.views.decorators.http import require_POST
from family.models import Photo, Album
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.shortcuts import Http404

@never_cache
def login(request):
    if request.user.is_authenticated():
        return redirect(LOGIN_REDIRECT_URL)

    form = CommonLoginForm()
    if request.POST.get('action', False) == 'common_login':
        user = auth.authenticate(
            username = request.POST.get('username'),
            password = request.POST.get('password'),
        )
        # If user exists
        if user is not None and user.is_active:
            auth.login(request, user)
            next = request.GET.get('next', False) or LOGIN_REDIRECT_URL
            return redirect(next)
        # If user does not exist or password is wrong
        else:
            form = CommonLoginForm(request.POST)
            messages.error(request, 'Your account does not exist or your password is wrong.')

    return render_to_response(
        'common/login.html',
        {'form' : form},
        RequestContext(request),
    )

def logout(request):
    auth.logout(request)
    return redirect(LOGOUT_REDIRECT_URL)

@require_POST
def delete(request):
    modelName = request.POST.get('modelName', None)
    try:
        if modelName == 'album':
            album = Album.objects.get(pk = request.POST.get('id'))
            if request.user == album.user or request.user.has_perm('family.delete_album'):
                album.delete()
            else:
                raise PermissionDenied
        elif modelName == 'photo':
            photo = Photo.objects.get(pk = request.POST.get('id')).delete()
            if request.user == photo.user or request.user.has_perm('family.delete_photo', photo):
                photo.delete()
            else:
                raise PermissionDenied
        else:
            raise ObjectDoesNotExist
    # If modelName does not exist or object does not exist
    except ObjectDoesNotExist:
        pass

    return redirect(request.POST.get('next', 'home_page'))

@require_POST
@user_passes_test(lambda u: u.is_superuser)
def empty_trash(request):
    Photo.objects.filter(album = None).delete()
    return redirect(request.POST.get('next', 'home_page'))