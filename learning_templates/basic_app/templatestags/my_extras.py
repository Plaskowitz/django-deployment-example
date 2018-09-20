from django import template

register = template.Library()

# or instead of line 14 you can write:
# @register.filter(name='cut')               stichwort decorators in python
def cut(value,arg):
    """
    This cuts out all values of arg from the stirng
    """

    return value.replace(arg,'')


register.filter('cut',cut)
