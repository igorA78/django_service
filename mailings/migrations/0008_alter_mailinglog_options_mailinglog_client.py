# Generated by Django 4.2.5 on 2023-09-26 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0007_alter_mailinglog_mailing_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailinglog',
            options={'verbose_name': 'Лог рассылки', 'verbose_name_plural': 'Логи рассылок'},
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mailings.client', verbose_name='Клиент'),
            preserve_default=False,
        ),
    ]
