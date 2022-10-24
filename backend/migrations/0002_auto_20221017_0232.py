# Generated by Django 3.2.16 on 2022-10-17 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acct_id', models.IntegerField(unique=True)),
                ('username', models.CharField(max_length=256, unique=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Twitter Accounts',
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='usercompany',
            options={'verbose_name': 'My Tracking List'},
        ),
        migrations.CreateModel(
            name='CompanyTwitterAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.company')),
                ('twitter_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.twitteraccount')),
            ],
            options={
                'verbose_name': 'Company Twitter Accounts',
            },
        ),
    ]