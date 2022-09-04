from django.db import models


class Weather(models.Model):
    now = models.IntegerField(verbose_name="Время сервера в формате Unixtime.")
    now_dt = models.CharField(max_length=255, verbose_name="Время сервера в UTC.")
    info = models.OneToOneField('Info', null=True, verbose_name="Информации о населенном пункте.",
                             on_delete=models.CASCADE, related_name='info')
    fact = models.OneToOneField('Fact', null=True, verbose_name="Фактической информации о погоде.",
                             on_delete=models.CASCADE, related_name='fact')
    client = models.OneToOneField('Requset_client_info', null=True,
                               verbose_name="Информацие о клиенте", on_delete=models.CASCADE, related_name='client')


class Info(models.Model):
    lat = models.IntegerField(null=True, verbose_name="Широта (в градусах).")
    lon = models.IntegerField(null=True, verbose_name="Долгота (в градусах).")
    tz = models.OneToOneField('Time_zone_info', null=True, verbose_name="Информация о часовом поясе.",
                           on_delete=models.CASCADE, related_name='tz')  # вернуться
    def_pressure_mm = models.IntegerField(null=True,
                                          verbose_name="Норма давления для данной координаты (в мм рт. ст.).")
    def_pressure_pa = models.IntegerField(null=True,
                                          verbose_name="Норма давления для данной координаты (в гектопаскалях).")
    url = models.CharField(null=True, max_length=255, verbose_name="Страница населенного пункта на сайте Яндекс.Погода")


class Time_zone_info(models.Model):
    offset = models.IntegerField(null=True, verbose_name="Часовой пояс в секундах от UTC")
    name = models.CharField(null=True, max_length=255, verbose_name="Название часового пояса.")
    abbr = models.CharField(null=True, max_length=255, verbose_name="Сокращенное название часового пояса.")
    dst = models.BooleanField(null=True, verbose_name="Признак летнего времени")


class Fact(models.Model):
    temp = models.IntegerField(null=True, verbose_name="Температура.")
    feels_like = models.IntegerField(null=True, verbose_name="Ощущаемая температура.")
    icon = models.CharField(null=True, max_length=255,
                            verbose_name="Код иконки погоды. Иконка доступна по адресу https://yastatic.net/weather/i/icons/funky/dark/<значение из поля icon>.svg.")
    condition = models.CharField(null=True, max_length=255, verbose_name="Код расшифровки погодного описания")


class Requset_client_info(models.Model):
    ip = models.GenericIPAddressField(null=True, verbose_name="iP адрес клиент")
    user_agent = models.CharField(max_length=1024, null=True, verbose_name="")
    request_time = models.DateTimeField(null=False, auto_now_add=True)
