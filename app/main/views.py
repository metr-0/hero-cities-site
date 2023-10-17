from django.views.generic import *
from django.views import View
from django.http import JsonResponse
import main.models


class MainPage(TemplateView):
    template_name = 'main/main.html'


class CityDetail(DetailView):
    model = main.models.City
    context_object_name = "city"
    template_name = "main/city.html"


class GetCities(View):
    template_name = "main/api.html"

    def get(self, request):
        return JsonResponse({
            "data": list(main.models.City.objects.points()),
        }, json_dumps_params={'ensure_ascii': False})
