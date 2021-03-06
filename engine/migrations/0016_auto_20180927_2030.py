# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0015_auto_20180622_0920'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='value',
            name='value_primary_idx',
        ),
        migrations.RemoveIndex(
            model_name='value',
            name='value_mooclet_idx',
        ),
        migrations.RemoveIndex(
            model_name='value',
            name='value_learner_idx',
        ),
        migrations.AlterUniqueTogether(
            name='mooclet',
            unique_together=set([]),
        ),
        migrations.AddIndex(
            model_name='value',
            index=models.Index(fields=['mooclet', 'learner', 'version'], name='engine_valu_mooclet_c50aaf_idx'),
        ),
        migrations.AddIndex(
            model_name='value',
            index=models.Index(fields=['mooclet'], name='engine_valu_mooclet_78bea6_idx'),
        ),
        migrations.AddIndex(
            model_name='value',
            index=models.Index(fields=['learner'], name='engine_valu_learner_00f366_idx'),
        ),
    ]
