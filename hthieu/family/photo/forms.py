from django import forms
from family.models import Photo

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model  = Photo
        exclude = ('created_at', 'updated_at', 'user', 'album', 'image', 'thumb')
        widgets = {
            'name'  : forms.TextInput(attrs = {'class':'span3', 'placeholder': 'Photo name'}),
            }
