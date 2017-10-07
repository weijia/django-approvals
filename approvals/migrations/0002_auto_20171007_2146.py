# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('approvals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='group_who_permit_to_act',
            field=models.ForeignKey(blank=True, to='auth.Group', help_text='Only users in this group can approve this request', null=True, verbose_name='Group of users who can approve'),
        ),
        migrations.AddField(
            model_name='approval',
            name='who_permit_to_act',
            field=models.ForeignKey(related_name='who_can_approve', blank=True, to=settings.AUTH_USER_MODEL, help_text='User who can approve this request', null=True, verbose_name='Users who can approve'),
        ),
        migrations.AlterField(
            model_name='approval',
            name='acted_on_by',
            field=models.ForeignKey(related_name='approved_by', blank=True, to=settings.AUTH_USER_MODEL, help_text='If this approval has been acted on, this will be the user that has made the decision.', null=True, verbose_name='acted on by'),
        ),
    ]
