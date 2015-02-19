# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150217_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_executor',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'\xd0\x9e\xd1\x82\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb0', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='posting_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
