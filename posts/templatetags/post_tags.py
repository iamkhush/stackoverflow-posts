from datetime import datetime
from django import template

register = template.Library()


@register.filter("parsetimestamp")
def timestamp(value):
    try:
        return datetime.fromtimestamp(value)
    except AttributeError:
        pass
