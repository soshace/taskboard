# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
