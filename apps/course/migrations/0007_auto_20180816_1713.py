# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-16 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20180816_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='download',
            field=models.FileField(max_length=200, upload_to='course/resource/%Y/%m', verbose_name='资源文件'),
        ),
    ]
