# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_auto_20170826_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='assignee',
            field=models.ForeignKey(related_query_name=b'assignee', related_name='assignee', blank=True, to='alerts.AlertAssignee', null=True),
        ),
        migrations.AlterField(
            model_name='alerts',
            name='manager',
            field=models.ForeignKey(related_query_name=b'manager', related_name='manager', blank=True, to='alerts.AlertManager', null=True),
        ),
    ]
