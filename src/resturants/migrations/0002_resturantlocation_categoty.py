# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-11 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturantlocation',
            name='categoty',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
