# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-15 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0053_auto_20190328_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='resumes/')),
                ('upload_to', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluator.Candidate')),
            ],
        ),
    ]