# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_language_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=300)),
            ],
        ),
    ]