# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-25 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='price',
            field=models.FloatField(),
        ),
    ]
