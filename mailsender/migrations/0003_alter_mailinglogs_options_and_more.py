# Generated by Django 4.2.4 on 2023-09-12 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailsender', '0002_mailing_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailinglogs',
            options={'verbose_name': 'Лог', 'verbose_name_plural': 'Логи'},
        ),
        migrations.RemoveField(
            model_name='mailinglogs',
            name='server_response',
        ),
        migrations.AddField(
            model_name='mailinglogs',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mailsender.client', verbose_name='Клиент'),
        ),
    ]
