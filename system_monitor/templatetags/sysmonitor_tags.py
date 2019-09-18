import psutil
from django              import template
from django.conf         import settings

try:
    path = settings.DISK_USAGE_PATH
except:
    path = "/"
register = template.Library()
@register.inclusion_tag('system_monitor/donut.html', takes_context=True)
def disk_donut(context):
    disk_usage = psutil.disk_usage(path)
    return {
        'disk_usage_free':disk_usage.percent,
    }
@register.simple_tag
def disk_text():
    disk_usage = psutil.disk_usage(path)
    return 'free space left (%): {}'.format(100 - disk_usage.percent)
