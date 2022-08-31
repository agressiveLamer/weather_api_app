# Generated by Django 4.1 on 2022-08-31 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_remove_fact_phenom_condition_remove_fact_temp_water'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requset_client_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.IntegerField(null=True, verbose_name='iP адрес клиент')),
                ('user_agent', models.CharField(max_length=1024, null=True, verbose_name='')),
                ('request_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='weather',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='weather.requset_client_info', verbose_name='Информацие о клиенте'),
        ),
    ]
