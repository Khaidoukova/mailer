from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}

class Client(models.Model):

    email = models.CharField(max_length=100, verbose_name='электронный адрес', unique=True)
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
        ('ежедневно', 'daily'),
        ('еженедельно', 'weekly'),
        ('ежемесячно', 'monthly'),
    ]

    STATUS_CHOICES = [
        ('created', 'создана'),
        ('запущена', 'running'),
        ('завершена', 'completed'),
    ]
    name = models.CharField(max_length=50, verbose_name='название', default='MyMailing')
    start_time = models.DateTimeField(default=timezone.now, verbose_name='Время запуска рассылки')
    stop_time = models.DateTimeField(default=timezone.now, verbose_name='Время завершения рассылки')
    frequency = models.CharField(max_length=15, default='ежемесячно', choices=FREQUENCY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=15, default='создана', choices=STATUS_CHOICES, verbose_name='статус рассылки')
    client = models.ManyToManyField(Client)
    title = models.CharField(max_length=50, verbose_name='тема письма', default='Message Title>')
    body = models.TextField(verbose_name='тело письма', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')

    def get_status(self):
        now = timezone.now()
        if self.start_time < now < self.stop_time:
            self.status = "running"
        elif now > self.stop_time:
            self.status = "completed"
        self.save()
        return self.status


    def __str__(self):
        return f"рассылка {self.name}, отправлена {self.start_time}(частота {self.frequency}, статус {self.status}"


    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class MailingLogs(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    last_try = models.DateTimeField(verbose_name='дата и время последней попытки', null=True, blank=True),
    status = models.CharField(max_length=15, choices=STATUSES, verbose_name='статус попытки'),
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', default=None)

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"






