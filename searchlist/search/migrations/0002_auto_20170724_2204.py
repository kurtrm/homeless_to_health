# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchprofile',
            name='age_range',
            field=models.CharField(choices=[('<=17', '<=17'), ('18-25', '18-25'), ('>26', '>26')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='searchprofile',
            name='ratings',
            field=models.CharField(choices=[('one badge', 'one badge'), ('two badge', 'two badge'), ('three badge', 'three badge')], default='one badge', max_length=25, null=True),
        ),
    ]
