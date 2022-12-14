from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
import requests
import json


class WeatherAPIView(APIView):
    __URL = "https://api.weather.yandex.ru/v2/forecast"
    __TOKEN = "bd8d3566-ebc3-4c69-91b4-874499c1c112"

    def post(self, request):
        """serializer = WeatherSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                save_result = serializer.save()"""
        r = request.data

        fact_weather_data_creater = Fact.objects.create(temp=r['fact']['temp'],
                                                        feels_like=r['fact']['feels_like'],
                                                        icon=r['fact']['icon'],
                                                        condition=r['fact']['condition'])
        tzinfo_weather_data_creater = Time_zone_info.objects.create(offset=r['info']['tzinfo']['offset'],
                                                                    name=r['info']['tzinfo']['name'],
                                                                    abbr=r['info']['tzinfo']['abbr'],
                                                                    dst=r['info']['tzinfo']['dst'])
        info_weather_data_creater = Info.objects.create(lat=r['info']['lat'],
                                                        lon=r['info']['lon'],
                                                        url=r['info']['url'],
                                                        tz=tzinfo_weather_data_creater,
                                                        def_pressure_mm=r['info']['def_pressure_mm'],
                                                        def_pressure_pa=r['info']['def_pressure_pa']
                                                        )

        save_result = Weather.objects.create(now=r['now'],
                                             now_dt=r['now_dt'],
                                             info=info_weather_data_creater,
                                             fact=fact_weather_data_creater
                                             )

        return Response({"Message": "???????????? ?????????????? ?????????????????? ?? ????",
                         "Record_id": save_result.pk})


    def get(self, request, **kwargs):
        client = request.META
        client_ip_address = client.get('REMOTE_ADDR')
        client_user_agent = client.get('HTTP_USER_AGENT')
        lat = kwargs.get('lat', None)
        lon = kwargs.get('lon', None)
        params = {"lat": lat,
                  "lon": lon
                  }
        headers = {"X-Yandex-API-Key": WeatherAPIView.__TOKEN}
        if lat == None:
            return Response({'Message': '????????????: ???????????? GET, ???? ???????????? lat ??????????????'})
        if lon == None:
            return Response({'Message': '????????????: ???????????? GET, ???? ???????????? lon ?????????????? '})
        else:
            yandex_request_response = requests.get(WeatherAPIView.__URL, params=params, headers=headers)
            bytes_json = yandex_request_response.content
            bytes_json_to_string = bytes_json.decode()
            decode_json = json.loads(bytes_json_to_string)
            client_creator = Requset_client_info.objects.create(ip=client_ip_address,
                                                                user_agent=client_user_agent)
            fact_creator = Fact.objects.create(temp=decode_json['fact']['temp'],
                                               feels_like=decode_json['fact']['feels_like'],
                                               icon=decode_json['fact']['icon'],
                                               condition=decode_json['fact']['condition'],
                                               )
            time_zone_info_creater = Time_zone_info.objects.create(name=decode_json['info']['tzinfo']['name'],
                                                                   abbr=decode_json['info']['tzinfo']['abbr'],
                                                                   dst=decode_json['info']['tzinfo']['dst'],
                                                                   offset=decode_json['info']['tzinfo']['offset'],
                                                                   )
            info_weather_creater = Info.objects.create(lon=decode_json['info']['lon'],
                                                       lat=decode_json['info']['lat'],
                                                       tz=time_zone_info_creater,
                                                       def_pressure_mm=decode_json['info']['def_pressure_mm'],
                                                       def_pressure_pa=decode_json['info']['def_pressure_pa'],
                                                       url=decode_json['info']['url'],
                                                       )

            response_id = Weather.objects.create(now=decode_json['now'],
                                                 now_dt=decode_json['now_dt'],
                                                 info=info_weather_creater,
                                                 fact=fact_creator,
                                                 client=client_creator
                                                 )
            return Response({"Message": "??????????????",
                             "Response_id": response_id.pk,
                             "Response_body": decode_json}
                            )
