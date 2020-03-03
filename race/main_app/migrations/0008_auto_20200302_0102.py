# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-03-02 01:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200229_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='runner',
            name='address',
            field=models.CharField(default='*', max_length=128),
        ),
        migrations.AddField(
            model_name='runner',
            name='birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='runner',
            name='blood_type',
            field=models.CharField(choices=[('O-', 'O -'), ('O+', 'O +'), ('A-', 'A -'), ('A+', 'A +'), ('B-', 'B -'), ('B+', 'B +'), ('AB-', 'AB -'), ('AB+', 'AB +')], default='O-', max_length=128),
        ),
        migrations.AddField(
            model_name='runner',
            name='cellphone',
            field=models.CharField(default='*', max_length=128, unique=True),
        ),
        migrations.AddField(
            model_name='runner',
            name='emergency_contact',
            field=models.CharField(default='*', max_length=128),
        ),
        migrations.AddField(
            model_name='runner',
            name='emergency_contact_cellphone',
            field=models.CharField(default='*', max_length=128),
        ),
        migrations.AddField(
            model_name='runner',
            name='first_lastname',
            field=models.CharField(default='*', max_length=128),
        ),
        migrations.AddField(
            model_name='runner',
            name='first_name',
            field=models.CharField(default='*', max_length=128),
        ),
        migrations.AddField(
            model_name='runner',
            name='gender',
            field=models.CharField(choices=[('ML', 'MASCULINO'), ('FM', 'FEMENINO'), ('OTHER', 'OTRO')], default='ML', max_length=128),
        ),
        migrations.AddField(
            model_name='runner',
            name='health',
            field=models.CharField(default='*', max_length=128),
        ),
        migrations.AddField(
            model_name='runner',
            name='second_lastname',
            field=models.CharField(default='*', max_length=128),
        ),
        migrations.AddField(
            model_name='runner',
            name='second_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='runner',
            name='document_number',
            field=models.CharField(default='*', max_length=128),
        ),
        migrations.AlterField(
            model_name='runner',
            name='email',
            field=models.EmailField(default='*', max_length=264, unique=True),
        ),
        migrations.RemoveField(
            model_name='runner',
            name='last_names',
        ),
        migrations.RemoveField(
            model_name='runner',
            name='names',
        ),
        migrations.AlterUniqueTogether(
            name='runner',
            unique_together=set([('document_type', 'document_number')]),
        ),
    ]
