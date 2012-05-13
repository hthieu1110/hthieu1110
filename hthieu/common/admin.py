from family.models import Album, Photo
from django.contrib import admin

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
admin.site.register(Album, AlbumAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'user', 'created_at')
    ordering = ['name']
admin.site.register(Photo, PhotoAdmin)






