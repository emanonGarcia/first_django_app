# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 13:55
from __future__ import unicode_literals
from django.db import migrations
from arsenal0304.models import Player
import csv


def load_data(apps, schema_editor):
    Player = apps.get_model("arsenal0304", "Player")
    csv_PATH = 'invincibles.csv'

    with open(csv_PATH, 'r') as f:
        catergories = {'fieldnames': ('kit_num', 'name', 'pos', 'dob', 'nat', 'apps', 'goals', 'assists', 'mins'), 'delimiter': ','}
        reader = csv.DictReader(f, **catergories)
        next(reader, None)

        for row in reader:
            p = Player(**row)
            p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('arsenal0304', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]