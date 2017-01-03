# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-22 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('stories', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, choices=[('Past events', 'Past events'), ('Opportunities', 'Opportunities')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('stories', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, choices=[('Local', 'Local'), ('Foreign', 'Foreign')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('story_type', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]