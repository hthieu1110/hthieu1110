from django import template
from family.photo.forms import PhotoUploadForm

register = template.Library()

@register.inclusion_tag('family/photo/forms/_uploadForm.html', takes_context = True)
def familyPhoto_renderUploadForm(context):
    request = context['request']
    photoForm = PhotoUploadForm()
    form  = hasattr(request, 'reboundedPhotoUploadForm') and request.reboundedPhotoUploadForm or photoForm
    return {'form': form}
