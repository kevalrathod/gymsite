# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime
# Create your models here.


USER_BODY_GOALS=(
    ('Bodybuilding','bodybuilding'),
    ('Strength','strength'),
    ('Lean','lean'),
    ('Shreded','shreded'),
    ('Bulk','bulk'),
    ('Weightlose','weightlose')
)

USER_MEAL_TYPE=(
    ('NON-VEG','nonveg'),
    ('VEG','veg')
)

class User(models.Model):
    fname=models.CharField(max_length=100,blank=True)
    lname=models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=70,blank=True)
    birth_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.email

class DietPlan(models.Model):
    height=models.IntegerField(blank=True)
    weight=models.IntegerField(blank=True)
    age=models.IntegerField(blank=True)
    bmi=models.IntegerField()
    user_goal=models.CharField(
            choices=USER_BODY_GOALS,
            default='bodybuilding',
            max_length=100)
    meal_type=models.CharField(
            choices=USER_MEAL_TYPE,
            default='veg',
            max_length=50)

