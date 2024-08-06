from django import template

register = template.Library()

@register.filter
def dict_item(dictionary, key):
    return dictionary.get(key)
