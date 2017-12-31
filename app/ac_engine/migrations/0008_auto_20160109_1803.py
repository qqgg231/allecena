# coding: utf-8
# Generated by Django 1.9 on 2016-01-09 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ac_engine', '0007_auto_20160109_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='provider',
            field=models.PositiveSmallIntegerField(choices=[(0, b'allegro'), (1, b'ebay'), (2, b'all')]),
        ),
        migrations.AlterField(
            model_name='triggers',
            name='provider',
            field=models.IntegerField(choices=[(0, b'allegro'), (1, b'ebay'), (2, b'all')]),
        ),
    ]
