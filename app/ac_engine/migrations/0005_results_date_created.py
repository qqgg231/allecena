# coding: utf-8
# Generated by Django 1.9 on 2016-01-08 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ac_engine', '0004_results_computing_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
