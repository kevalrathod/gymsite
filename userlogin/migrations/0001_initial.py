# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-21 17:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(blank=True)),
                ('weight', models.IntegerField(blank=True)),
                ('age', models.IntegerField(blank=True)),
                ('bmi', models.IntegerField()),
                ('user_goal', models.CharField(choices=[('Bodybuilding', 'bodybuilding'), ('Strength', 'strength'), ('Lean', 'lean'), ('Shreded', 'shreded'), ('Bulk', 'bulk'), ('Weightlose', 'weightlose')], default='bodybuilding', max_length=100)),
                ('meal_type', models.CharField(choices=[('NON-VEG', 'nonveg'), ('VEG', 'veg')], default='veg', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=100)),
                ('lname', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('birth_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]