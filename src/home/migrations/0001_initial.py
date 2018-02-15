# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-04 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=60)),
                ('student_name', models.CharField(max_length=25)),
                ('secratary_name', models.CharField(max_length=25)),
                ('incharge_name', models.CharField(max_length=25)),
                ('cricket_boys', models.BooleanField(default=False)),
                ('football_boys', models.BooleanField(default=False)),
                ('basketball_boys', models.BooleanField(default=False)),
                ('volleyball_boys', models.BooleanField(default=False)),
                ('squash_boys', models.BooleanField(default=False)),
                ('lawn_tennis_boys', models.BooleanField(default=False)),
                ('badminton_boys', models.BooleanField(default=False)),
                ('atheletics_boys', models.BooleanField(default=False)),
                ('triathlon_boys', models.BooleanField(default=False)),
                ('table_tennis_boys', models.BooleanField(default=False)),
                ('swimming_boys', models.BooleanField(default=False)),
                ('snookers_boys', models.BooleanField(default=False)),
                ('carrom_boys', models.BooleanField(default=False)),
                ('chess_boys', models.BooleanField(default=False)),
                ('basketball_girls', models.BooleanField(default=False)),
                ('volleyball_girls', models.BooleanField(default=False)),
                ('squash_girls', models.BooleanField(default=False)),
                ('lawn_tennis_girls', models.BooleanField(default=False)),
                ('badminton_girls', models.BooleanField(default=False)),
                ('atheletics_girls', models.BooleanField(default=False)),
                ('triathlon_girls', models.BooleanField(default=False)),
                ('table_tennis_girls', models.BooleanField(default=False)),
                ('swimming_girls', models.BooleanField(default=False)),
                ('snookers_girls', models.BooleanField(default=False)),
                ('carrom_girls', models.BooleanField(default=False)),
                ('chess_girls', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=25)),
                ('faculty_email', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=25)),
                ('secratary_phone_number', models.CharField(max_length=25)),
            ],
        ),
    ]