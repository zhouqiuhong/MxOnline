# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-16 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='访问地址'),
        ),
    ]