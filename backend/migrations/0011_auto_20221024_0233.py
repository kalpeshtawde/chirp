# Generated by Django 3.2.16 on 2022-10-24 02:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_usertweet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertweet',
            options={'verbose_name': 'UserTweet'},
        ),
        migrations.AddField(
            model_name='usertweet',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usertweet',
            name='message_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertweet',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]