# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-12 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='sistemas',
        ),
        migrations.AddField(
            model_name='projeto',
            name='sistemas',
            field=models.ManyToManyField(related_name='_projeto_sistemas_+', to='pmo.Sistema'),
        ),
    ]
