from django import template

register = template.Library()


@register.filter
def myfunc(value):
    return value.upper()


@register.simple_tag
def mytag1():
    return "hhhhh"


@register.simple_tag
def mytag2(a1, a2):
    return a1 + 'hhhh' + a2


@register.inclusion_tag("app01/xxxx.html")
def xxx():
    return {"name": 'age', "age": 123}
