# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approvals', '0003_auto_20171008_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='is_send_notification_now',
            field=models.BooleanField(default=True),
        ),
    ]
