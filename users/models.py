from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    STATUS_ACTIVE = 'active'
    STATUS_BLOCKED = 'blocked'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'активен'),
        (STATUS_BLOCKED, 'заблокирован'),
    ]
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    register_key = models.CharField(max_length=15, verbose_name='Ключ подтверждения регистрации', default='')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Статус', default=STATUS_ACTIVE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            (
                'moderator',
                'can moderate mailings and users'
            )
        ]
