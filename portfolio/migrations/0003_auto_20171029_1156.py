# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20171029_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='endDate',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='startDate',
            field=models.DateTimeField(blank=True),
        ),
    ]
