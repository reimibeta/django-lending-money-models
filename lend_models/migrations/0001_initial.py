# Generated by Django 3.1.7 on 2021-06-15 08:36

import datetime_utils.date_time
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallet_models', '0004_delete_walletadjust'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lend_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
            ],
        ),
        migrations.CreateModel(
            name='LendClientSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LendClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
                ('updated_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lend_models.lendclientset')),
            ],
        ),
        migrations.CreateModel(
            name='LendAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=20, null=True)),
                ('note', models.CharField(blank=True, max_length=250, null=True)),
                ('is_return', models.BooleanField(default=False)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet_models.wallet')),
                ('lend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lend_models.lend')),
            ],
        ),
        migrations.AddField(
            model_name='lend',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lend_models.lendclient'),
        ),
    ]
