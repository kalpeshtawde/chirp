# Generated by Django 3.2.16 on 2022-10-23 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_telegramaccount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegramaccount',
            options={'verbose_name': 'Telegram Account'},
        ),
        migrations.AlterField(
            model_name='tweets',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
