# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vital', '0003_virtual_machines_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtual_machines',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vital.Virtual_Machine_Type'),
        ),
    ]
