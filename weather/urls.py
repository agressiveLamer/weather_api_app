from django.urls import path, re_path
from .views import *

urlpatterns = [
    # path('api/v1/weather/lat=<str:lat>/lon=<str:lon>', WeatherAPIView.as_view())
    re_path(r'api/v1/weather/lat=(?P<lat>[0-9.]{1,})/lon=(?P<lon>[0-9.]{1,})$', WeatherAPIView.as_view())
]
