from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    email_is_confirmed = models.BooleanField(default=False, verbose_name='подтверждено')
    email_confirm_key = models.CharField(max_length=30, verbose_name='код подтверждения почты', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        permissions = [
            ('block_another_user', 'Can block another user'),
        ]

