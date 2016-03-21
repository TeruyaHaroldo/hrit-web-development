# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_content_apresentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='apresentation',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
