# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-04 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_classifier_accuracy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classifier',
            name='accuracy',
        ),
    ]
