from django.urls import path

from .views import *

app_name = "main"

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world'),
    path('<int:pk>', CityDetail.as_view(), name='city_detail'),
]
