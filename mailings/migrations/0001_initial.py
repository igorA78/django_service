# Generated by Django 4.2.5 on 2023-09-10 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('desription', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('sending_time_start', models.TimeField(default=datetime.time(10, 0), verbose_name='Время отправки (с)')),
                ('sending_time_end', models.TimeField(default=datetime.time(11, 0), verbose_name='Время отправки (до)')),
                ('periodicity', models.CharField(choices=[('once', 'Один раз'), ('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], default='once', max_length=20, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('done', 'Завершена')], default='created', max_length=20, verbose_name='Статус')),
                ('mail_title', models.CharField(max_length=300, verbose_name='Тема письма')),
                ('mail_content', models.TextField(verbose_name='Содержание письма')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
