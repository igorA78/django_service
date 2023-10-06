# Generated by Django 4.2.5 on 2023-09-25 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0004_rename_desription_mailing_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_date', models.DateField(auto_now_add=True, verbose_name='Дата отправки')),
                ('mailing_time', models.TimeField(auto_now_add=True, verbose_name='Время отправки')),
                ('status', models.CharField(choices=[('success', 'Отправлено'), ('fail', 'Ошибка')], max_length=10, verbose_name='Статус')),
                ('server_ans', models.CharField(max_length=150, verbose_name='Ответ сервера')),
            ],
            options={
                'verbose_name': 'Лог рассылки',
                'verbose_name_plural': 'Логи рассылки',
            },
        ),
    ]