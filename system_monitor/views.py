from django.views.generic.base 		import TemplateView

# Create your views here.
class Test(TemplateView):
    template_name = "system_monitor/test.html"
