# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='orca_cards_available',
            field=models.BooleanField(default=False),
        ),
    ]