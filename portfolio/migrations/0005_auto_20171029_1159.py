# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20171029_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.IssueTracker'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='todoList',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.TodoList'),
        ),
    ]
