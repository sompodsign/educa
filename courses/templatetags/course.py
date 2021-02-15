from django import template

register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj.__meta.model_name
    except AttributeError:
        return None
