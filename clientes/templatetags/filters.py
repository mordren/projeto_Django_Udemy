from django import template

register = template.Library()

@register.filter
def my_filter(data):
    return data + ' -- ' + 'Alterado via Filter'

@register.filter
def arredondar(data, casa):
    return round(data, casa)

