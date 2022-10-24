# Generated by Django 3.2.16 on 2022-10-23 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20221023_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='tweet_id',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='acct_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
