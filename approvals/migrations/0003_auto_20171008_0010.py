# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approvals', '0002_auto_20171007_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='message_template',
            field=models.CharField(max_length=1024, null=True, verbose_name='message template', blank=True),
        ),
        migrations.AddField(
            model_name='approval',
            name='subject_template',
            field=models.CharField(max_length=1024, null=True, verbose_name='subject template', blank=True),
        ),
    ]
