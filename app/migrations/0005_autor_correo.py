# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160711_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='correo',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
