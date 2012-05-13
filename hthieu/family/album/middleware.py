from family.album.forms import AlbumNewForm
from family.models import Album
from django.contrib import messages
from django.shortcuts import redirect

class AlbumNewMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # If action = post_comment
        if request.POST.get('action', False) == 'create_album':
            form = AlbumNewForm(request.POST)
            # If there is no error(errors from user) then process the form
            if form.is_valid():
                album = Album(
                    name = form.cleaned_data['name'],
                    user = request.user
                )

                # Save the album only in case of it does not exist
                if not album.isExists():
                    album.save()
                    # Success flash message
                    messages.success(request, 'Album "' + album.name + '" has been created successfully.')

                # If the album already exist
                else:
                    # Error flash message
                    messages.error(request, 'Album "' + album.name + '" already exists.')

                # Always redirect once the form is submitted and processed
                return redirect(request.path)

            # If there are some form errors(errors from user)
            else:
                request.reboundedAlbumNewForm  = form
                # Error flash message
                messages.error(request, 'Please verify your album.')

        # If action is not album creating
        else:
            return None