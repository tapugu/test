from django import template
register = template.Library()


@register.filter
def get_dictionary(value, dic):
    return dic[value]
