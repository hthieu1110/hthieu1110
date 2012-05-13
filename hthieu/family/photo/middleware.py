from family.settings import PHOTO_SIZE, THUMB_SIZE
from family.models import Album, Photo
from family.photo.forms import PhotoUploadForm

from django.core.files.base import ContentFile
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from time import strftime
import random

class PhotoUploadMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # If action = upload_photo
        if request.POST.get('action', False) == 'upload_photo':
            form = PhotoUploadForm(request.POST, request.FILES)
            # If there is no error(errors from user) then process the form

            if form.is_valid():
                album = get_object_or_404(Album, pk = view_kwargs['album_id'])
                photo = Photo(
                    user = request.user,
                    album = album,
                    name = form.cleaned_data['name'],
                )

                rand = strftime('%H_%M_%S') + '_' + random.choice('abcdefghijklmnopqrstuvxywz')
                image_origin_file_name =  rand + '.origin.jpg'
                image_file_name = rand + '.jpg'
                thumb_file_name = rand + '.thumb.jpg'

                file_data = ContentFile(request.FILES['image_origin'].read())

                photo.image_origin.save(image_origin_file_name, file_data, save = False)
                photo.image.save(image_file_name, ContentFile(photo.image_origin.read()), save = False, size = PHOTO_SIZE)
                photo.thumb.save(thumb_file_name, ContentFile(photo.image.read()), save = False, size = THUMB_SIZE)
                photo.save()

                messages.success(request, 'Your photo has been uploaded successfully.')

                # Always redirect once the form is submitted and processed
                return redirect(request.path)

            # If there are some form errors(errors from user)
            else:
                request.reboundedPhotoUploadForm  = form
                # Error flash message
                messages.error(request, 'Please verify your photo.')

        # If action is not photo uploading
        else:
            return None