from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import time, datetime

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):

    email = models.CharField(max_length=100, verbose_name='электронный адрес')
    name = models.CharField(max_length=50, verbose_name='имя получателя')
    comment = models.TextField(verbose_name='комментарий', null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец клиента', **NULLABLE)

    def __str__(self):
        return f'Email: {self.email} ({self.name})'

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"

class Mailing(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'ежедневно'),
        ('weekly', 'еженедельно'),
        ('monthly', 'ежемесячно'),
    ]

    STATUS_CHOICES = [
        ('created', 'создана'),
        ('running', 'запущена'),
        ('completed', 'завершена'),
    ]
    name = models.CharField(max_length=50, verbose_name='название', default='MyMailing')
    start_time = models.TimeField(default=timezone.now, verbose_name='Время запуска рассылки')
    next_start = models.DateField(default=timezone.now, verbose_name='дата запуска рассылки')
    stop_time = models.TimeField(default=timezone.now, verbose_name='Время завершения рассылки')
    frequency = models.CharField(max_length=15, default='ежемесячно', choices=FREQUENCY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=15, default='создана', choices=STATUS_CHOICES, verbose_name='статус рассылки')
    client = models.ManyToManyField(Client, **NULLABLE, verbose_name='подписчики')
    title = models.CharField(max_length=50, verbose_name='тема письма', default='Message Title')
    body = models.TextField(verbose_name='тело письма', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец рассылки',
                              **NULLABLE)
    def get_status(self):
        now = datetime.now().time()
        print(self.start_time)
        print(now)
        print(self.stop_time)
        if self.start_time < now < self.stop_time:
            self.status = "running"

            self.save()
        return self.status


    def __str__(self):
        return f"{self.name}"


    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ('change_mailing_status', 'Can change mailing status'),
        ]


class MailingLogs(models.Model):

    STATUSES = [
        ('ok', 'Успешно'),
        ('failed', 'Ошибка'),
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    last_try = models.DateTimeField(verbose_name='дата и время последней попытки', null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUSES, default='ok', verbose_name='статус попытки')

    def __str__(self):
        return self.last_try


    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"






