from django.views.generic import *

from main.models import *


class HelloWorld(TemplateView):
    template_name = 'main/main.html'
