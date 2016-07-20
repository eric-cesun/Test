# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160711_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='libro',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Autor'),
        ),
    ]