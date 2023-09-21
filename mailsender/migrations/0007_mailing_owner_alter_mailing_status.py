# Generated by Django 4.2.4 on 2023-09-20 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailsender', '0006_remove_mailing_sending_time_mailing_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='владелец рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('создана', 'created'), ('запущена', 'running'), ('завершена', 'completed')], default='создана', max_length=15, verbose_name='статус рассылки'),
        ),
    ]
