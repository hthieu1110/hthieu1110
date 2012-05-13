from django import template
from family.album.forms import AlbumNewForm

register = template.Library()

@register.inclusion_tag('family/album/forms/_newForm.html', takes_context = True)
def familyAlbum_renderNewForm(context):
    request = context['request']
    albumNewForm = AlbumNewForm()
    form  = hasattr(request, 'reboundedAlbumNewForm') and request.reboundedAlbumNewForm or albumNewForm
    return {'form': form}