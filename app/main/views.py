from django.views.generic import *

from main.models import *


class HelloWorld(TemplateView):
    template_name = 'main/hello_world.html'
