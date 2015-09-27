# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe6\xa0\x87\xe9\xa2\x98', max_length=30, verbose_name='title')),
                ('content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('author', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile(b'^\\w$'), 'Please input valid author name', b'invalid')])),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
