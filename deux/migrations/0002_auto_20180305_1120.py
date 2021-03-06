# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-05 11:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deux', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multifactorauth',
            name='email',
            field=models.EmailField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='multifactorauth',
            name='challenge_type',
            field=models.CharField(blank=True, choices=[('sms', 'SMS'), ('', 'Off'), ('email', 'EMAIL')], default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='multifactorauth',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number.', regex='^(\\+?\\d{7,15})$')]),
        ),
    ]
