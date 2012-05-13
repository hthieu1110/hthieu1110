from django.db import models
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from common.fields import JPEGImageField

class FamilyModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField('created_at', auto_now_add = True)
    updated_at = models.DateTimeField('updated_at', auto_now = True)

class Album(FamilyModel):
    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    name = models.CharField(max_length = 255)
    public = models.BooleanField(default = False)

    class Meta:
        permissions = (
        )

    def isExists(self):
        try:
            album = Album.objects.get(name = self.name)
        except Album.DoesNotExist:
            return False

        return True

    def getLastUploadedPhoto(self):
        try:
            photo = self.photo_set.all().order_by('-created_at')[:1][0]
        except IndexError:
            return None
        return photo

    def __unicode__(self):
        return self.name

class Photo(FamilyModel):
    album        = models.ForeignKey(Album, null = True, on_delete = models.SET_NULL)
    user         = models.ForeignKey(User)
    name         = models.CharField(max_length = 255)
    image_origin = JPEGImageField(upload_to = 'photos/%Y/%m/%d')
    image        = JPEGImageField(upload_to = 'photos/%Y/%m/%d')
    thumb        = JPEGImageField(upload_to = 'photos/%Y/%m/%d')

    def __unicode__(self):
        return self.name

# Definition of handler of signal post_delete
# Because querySet.delete() of Admin will not execute custom delete of object
@receiver(pre_delete, sender = Photo)
def photo_deleteImages(sender, **kwargs):
    photo = kwargs['instance']
    try:
        photo.image_origin.delete()
        photo.image.delete()
        photo.thumb.delete()
    except OSError:
        pass
