# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchlist', '0017_resource_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(db_index=True, max_length=256)),
                ('value', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='resource',
            name='street',
            field=models.CharField(blank=True, default='', max_length=256),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='resource',
            name='tags',
        ),
        migrations.AlterField(
            model_name='resource',
            name='website',
            field=models.URLField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='resourcetag',
            unique_together=set([('family', 'value')]),
        ),
    ]
