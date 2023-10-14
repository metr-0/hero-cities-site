from django.views.generic import *

import main.models


class HelloWorld(TemplateView):
    template_name = 'main/main.html'


class CityDetail(DetailView):
    model = main.models.City
    context_object_name = "city"
    template_name = "main/city_detail.html"


class GetCities(TemplateView):
    template_name = "main/api.html"

    def get_context_data(self, **kwargs):
        context = {
            "data": list(main.models.City.objects.points()),
        }
        return context

