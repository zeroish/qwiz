# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-11-07 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20171103_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.SlugField(max_length=5, unique=True),
        ),
    ]
