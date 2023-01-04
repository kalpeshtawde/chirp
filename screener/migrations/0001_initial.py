# Generated by Django 3.2.16 on 2023-01-04 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('exch_name', models.CharField(max_length=50)),
                ('exch_code', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Q', 'Quarterly'), ('A', 'Annually')], default='Q', max_length=20)),
                ('sales', models.IntegerField(blank=True, null=True, unique=True)),
                ('expenses', models.IntegerField(blank=True, null=True, unique=True)),
                ('operating_profit', models.IntegerField(blank=True, null=True, unique=True)),
                ('opm', models.IntegerField(blank=True, null=True, unique=True)),
                ('other_income', models.IntegerField(blank=True, null=True, unique=True)),
                ('interest', models.IntegerField(blank=True, null=True, unique=True)),
                ('depreciation', models.IntegerField(blank=True, null=True, unique=True)),
                ('profit_before_tax', models.IntegerField(blank=True, null=True, unique=True)),
                ('tax', models.IntegerField(blank=True, null=True, unique=True)),
                ('net_profit', models.IntegerField(blank=True, null=True, unique=True)),
                ('eps', models.IntegerField(blank=True, null=True, unique=True)),
                ('currency', models.CharField(choices=[('INR', 'Indian Rupees'), ('USD', 'American Dollar')], default='INR', max_length=20)),
                ('unit', models.CharField(blank=True, max_length=20, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screener.company')),
            ],
        ),
    ]
