from django.template import Library

register = Library()

@register.filter()
def check(value):
    try:
        return float(value)
    except ValueError:
        return None