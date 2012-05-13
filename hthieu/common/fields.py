from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^common\.fields\.JPEGImageField"])

import Image
import cStringIO

from django.core.files.base import ContentFile
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile

class JPEGImageFieldFile(ImageFieldFile):

    def save(self, name, content, save=True, size = ()):
        if content:
            image = Image.open(content)
            if image.mode not in ('L', 'RGB'):
                image = image.convert("RGB")

            if len(size) == 2:
                image = self._resize(image, size)

            buf = cStringIO.StringIO()
            image.save(buf, format="JPEG")
            new_content_str = buf.getvalue()
            content = ContentFile(new_content_str)

        return super(JPEGImageFieldFile, self).save(name, content, save)

    def _resize(self, image, size):
        _width = size[0]
        _height = size[1]

        old_width = image.size[0]
        old_height = image.size[1]

        new_width = _width
        new_height = new_width * old_height / old_width

        if new_height > _height:
            new_height = _height
            new_width = new_height * old_width / old_height

        return image.resize((new_width, new_height), Image.ANTIALIAS)

class JPEGImageField(ImageField):
    """
    ImageField that converts all images to JPEG on save.
    """
    attr_class = JPEGImageFieldFile
