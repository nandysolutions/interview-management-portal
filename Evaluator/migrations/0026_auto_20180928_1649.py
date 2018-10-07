# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 11:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0025_round_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RatingSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate_min', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('rate_max', models.IntegerField(default=6, validators=[django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.AddField(
            model_name='aspect',
            name='rating_sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluator.RatingSheet'),
        ),
    ]
