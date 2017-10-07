# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approved', models.NullBooleanField(help_text="Has the 'needs_approval' object been approved, turned down, or not acted on yet.", verbose_name='approved')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created', db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('when_acted_on', models.DateTimeField(null=True, verbose_name='when acted on', blank=True)),
                ('reason', models.TextField(help_text='When an object is approved or disapproved the person doing the action can supply some reason here.', max_length=2048, null=True, verbose_name='reason', blank=True)),
                ('object_id', models.PositiveIntegerField(verbose_name='object id')),
                ('acted_on_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, help_text='If this approval has been acted on, this will be the user that has made the decision.', null=True, verbose_name='acted on by')),
                ('content_type', models.ForeignKey(verbose_name='content type', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'approval',
                'verbose_name_plural': 'approvals',
            },
        ),
    ]
