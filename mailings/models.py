import datetime

from django.db import models

from main.models import NULLABLE
from users.models import User


class Mailing(models.Model):
    PERIOD_ONCE = 'once'
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_ONCE, 'Один раз'),
        (PERIOD_DAILY, 'Раз в день'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'
    STATUSES = (
        (STATUS_CREATED, 'Создана'),
        (STATUS_STARTED, 'Запущена'),
        (STATUS_DONE, 'Завершена'),
    )

    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    sending_time_start = models.TimeField(verbose_name='Время отправки (с)', default=datetime.time(10, 0))
    sending_time_end = models.TimeField(verbose_name='Время отправки (до)', default=datetime.time(11, 0))
    periodicity = models.CharField(max_length=20, choices=PERIODS, verbose_name='Периодичность',
                                   default=PERIOD_ONCE)
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='Статус',
                              default=STATUS_CREATED)

    mail_title = models.CharField(max_length=300, verbose_name='Тема письма')
    mail_content = models.TextField(verbose_name='Содержание письма')

    # user_admin = User.objects.get(email='admin@mail.com').pk
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    email = models.EmailField(verbose_name='Почта')
    first_name = models.CharField(max_length=50, **NULLABLE, verbose_name='Имя')
    last_name = models.CharField(max_length=50, **NULLABLE, verbose_name='Фамилия')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return f'{self.email} ({self.first_name} {self.last_name})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class MailingLog(models.Model):
    STATUS_SUCCESS = 'success'
    STATUS_FAIL = 'fail'
    STATUSES = (
        (STATUS_SUCCESS, 'Отправлено'),
        (STATUS_FAIL, 'Ошибка'),
    )

    mailing_date = models.DateField(auto_now_add=True, verbose_name='Дата отправки')
    mailing_time = models.TimeField(auto_now_add=True, verbose_name='Время отправки')
    status = models.CharField(max_length=10, choices=STATUSES, verbose_name='Статус')
    server_ans = models.CharField(max_length=150, verbose_name='Ответ сервера', **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    def __str__(self):
        return f'{self.mailing_date} {self.mailing_time} ({self.status})'

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылок'
