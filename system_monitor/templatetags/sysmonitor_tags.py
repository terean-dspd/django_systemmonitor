import psutil
from django              import template
from django.conf         import settings


register = template.Library()
@register.inclusion_tag('system_monitor/donut.html', takes_context=True)
def disk_donut(context):
    try:
        path = settings.DISK_USAGE_PATH
    except:
        path = "/"
    disk_usage = psutil.disk_usage(path)
    return {
        'disk_usage_free':disk_usage.percent,
    }
