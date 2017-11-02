# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20171029_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]