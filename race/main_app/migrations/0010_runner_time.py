# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-03-02 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200302_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='runner',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
