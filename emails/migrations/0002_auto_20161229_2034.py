# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-29 19:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='friends_family',
            new_name='friends_and_family',
        ),
    ]