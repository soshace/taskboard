# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('posting_date', models.DateField()),
                ('cost', models.FloatField()),
                ('author', models.ForeignKey(related_name='task_author', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(related_name='task_executor', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cash', models.FloatField(default=0.0)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_executor', models.BooleanField(default=False)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
