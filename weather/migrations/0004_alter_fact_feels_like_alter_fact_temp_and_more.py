# Generated by Django 4.1 on 2022-08-31 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_remove_info_abbr_remove_info_dst_remove_info_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='feels_like',
            field=models.IntegerField(null=True, verbose_name='Ощущаемая температура.'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='temp',
            field=models.IntegerField(null=True, verbose_name='Температура.'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='temp_water',
            field=models.IntegerField(null=True, verbose_name='Температура воды.'),
        ),
        migrations.AlterField(
            model_name='info',
            name='def_pressure_mm',
            field=models.IntegerField(null=True, verbose_name='Норма давления для данной координаты (в мм рт. ст.).'),
        ),
        migrations.AlterField(
            model_name='info',
            name='def_pressure_pa',
            field=models.IntegerField(null=True, verbose_name='Норма давления для данной координаты (в гектопаскалях).'),
        ),
        migrations.AlterField(
            model_name='time_zone_info',
            name='offset',
            field=models.IntegerField(null=True, verbose_name='Часовой пояс в секундах от UTC'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='now',
            field=models.IntegerField(verbose_name='Время сервера в формате Unixtime.'),
        ),
    ]