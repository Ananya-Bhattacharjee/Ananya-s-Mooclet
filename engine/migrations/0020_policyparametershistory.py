# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-28 22:44
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0019_auto_20181210_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyParametersHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('mooclet', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='engine.Mooclet')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Policy')),
            ],
            options={
                'verbose_name_plural': 'policyparameterhistories',
            },
        ),
    ]
