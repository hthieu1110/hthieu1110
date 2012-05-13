from django import template

register = template.Library()

@register.inclusion_tag('family/_rightMenu.html', takes_context = True)
def familyPartial_renderRightMenu(context):
    request = context['request']
    return {'a':'b'}
