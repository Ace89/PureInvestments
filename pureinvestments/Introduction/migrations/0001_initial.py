# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_name', models.CharField(max_length=200)),
                ('message_contact', models.CharField(max_length=200)),
                ('message_body', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name=b'date submitted')),
            ],
        ),
    ]
