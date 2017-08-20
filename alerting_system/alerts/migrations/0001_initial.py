# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertAssignee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AlertManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_id', models.CharField(max_length=100)),
                ('delay', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('assignee', models.ForeignKey(related_query_name=b'assignee', related_name='assignee', to='alerts.AlertAssignee')),
                ('manager', models.ForeignKey(related_query_name=b'manager', related_name='manager', to='alerts.AlertManager')),
            ],
        ),
    ]
