# Generated by Django 4.2.4 on 2023-09-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('active', 'активен'), ('blocked', 'заблокирован')], default='blocked', max_length=15, verbose_name='статус пользователя'),
        ),
    ]
