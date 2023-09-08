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
    sending_time = models.DateTimeField(default=timezone.now, verbose_name='Время рассылки')
    frequency = models.CharField(max_length=15, default='ежемесячно', choices=FREQUENCY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=15, default='создана', choices=STATUS_CHOICES, verbose_name='статус рассылки')
    client = models.ManyToManyField(Client)

    def __str__(self):
        return f"рассылка {self.pk}, отправлена {self.sending_time}(частота {self.frequency}, статус {self.status}"


    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

class Message(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    title = models.CharField(max_length=50, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f"Письмо {self.title}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class MailingLogs(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    last_try = models.DateTimeField(verbose_name='дата и время последней попытки', null=True, blank=True),
    status = models.CharField(max_length=15, verbose_name='статус попытки'),
    server_response = models.CharField(max_length=200, verbose_name='ответ почтового сервера', null=True, blank=True)






