# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20171110_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='features',
            field=models.ManyToManyField(to='portfolio.Features'),
        ),
    ]