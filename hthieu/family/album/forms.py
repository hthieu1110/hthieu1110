from django import forms
from family.models import Album

class AlbumNewForm(forms.ModelForm):
    class Meta:
        model  = Album
        exclude = ('created_at', 'updated_at', 'user', 'public')
        widgets = {
            'name'    : forms.TextInput(attrs = {'class':'span3', 'placeholder': 'Album name'}),
        }
