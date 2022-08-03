from django import template
from time import mktime

register = template.Library()

def substract_time(value1, value2):
    delta = mktime( value1.timetuple()) - mktime(value2.timetuple())
    if delta <60:
        delta = "أقل من"
    else:
        delta = int(delta/60) + 1
    return delta

register.filter('substract_time', substract_time)