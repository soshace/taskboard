# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskBoardSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commission', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
