# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-02-28 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='runner',
            old_name='first_name',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='runner',
            old_name='last_name',
            new_name='nombres',
        ),
    ]
