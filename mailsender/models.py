from django.db import models
from django.utils import timezone


# Create your models here.
class Client(models.Model):

    email = models.CharField(max_length=100, verbose_name='электронный адрес')
    name = models.CharField(max_length=50, verbose_name='имя получателя')
    comment = models.TextField(verbose_name='комментарий', null=True, blank=True)



    def __str__(self):
        return f'Email: {self.email} ({self.surname} {self.name})'

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"

class Mailing:
    FREQUENCY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('running', 'Запущена'),
        ('completed', 'Завершена'),
    ]
    sending_time = models.DateTimeField(default=timezone.now, verbose_name='Время рассылки')
    frequency = models.CharField(max_length=15, choices=FREQUENCY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name='статус рассылки')

    def __str__(self):
        return f"рассылка {self.pk}, отправлена {self.sending_time}(частота {self.frequency}, статус {self.status}"


    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"






