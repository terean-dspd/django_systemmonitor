=====
Django System Monitor
=====

Monitors disk usage and shows it as doughnut chart

Quick start
-----------

1. Add "system_monitor" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'system_monitor',
    ]

2. Optionally add
    DISK_USAGE_PATH = "path_to_monitor"
    to your settings.py file. There DISK_USAGE_PATH is the given path to monitor.
    By default is "/".

3. Add {% load sysmonitor_tags %} at the beginning of your template(s) where you
   want to display usage statistics

4. Add {% disk_doughnut %} tag to show chart
