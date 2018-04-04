# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from django.shortcuts import redirect
from datetime import datetime

class Position(models.Model):
    name = models.CharField(max_length=50)
    id_code = models.CharField(max_length=10)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=40)
    contact_validator = RegexValidator(regex='\d+')
    contact_primary = models.CharField(max_length=20, validators=[contact_validator], null=True)
    experience = models.PositiveIntegerField()
    position_applied = models.ForeignKey(Position)


    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=200, default='Exam')
    total_questions = models.IntegerField(default=4)
    times_taken = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return "/exam/%s" % self.name


class Interview(models.Model):
    candidate = models.ForeignKey(Candidate)
    date = models.DateField()
    position = models.ForeignKey(Position)
    exam = models.ForeignKey(Exam, null=True)
    status_choices = (
        ('AC', 'Active'),
        ('CN', 'Cancelled'),
        ('FN', 'Finished'),
                     )
    status = models.CharField(
                        max_length=2,
                        choices=status_choices,
                        default='AC'
                             )

    # This is to mark if the candidate passed the test.
    result_choices = (
        ('P', 'Pass'),
        ('F', 'Fail'),
        ('TBD', 'Pending'),
                    )

    result = models.CharField(
        max_length=3,
        choices=result_choices,
        default='TBD'
    )

    def __str__(self):  # __unicode__ on Python 2
        return "{0}_{1}_{2}".format(self.candidate, str(self.date), self.position)

    def interviews_today(self):
        return Interview.objects.filter(date=datetime.today())

    def all_interviews(self):
        return Interview.objects.all()

class Skill(models.Model):
    name = models.CharField('Name', max_length=20)
    position = models.ManyToManyField(Position)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

   
 
class Question(models.Model):
    description = models.CharField('Description', max_length=300)
    difficulty_choice = (
        ('H', 'Hard'),
        ('M', 'Medium'),
        ('E', 'Easy'),
    )

    difficulty = models.CharField(
        max_length=3,
        choices=difficulty_choice,
        default='M'
                    )

    skill = models.ForeignKey(Skill, null=True)
    exam = models.ForeignKey(Exam, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return "{0}".format(self.description)


class Answer(models.Model):
    """
    Answer's Model, which is used as the answer in Question Model
    """
    detail = models.CharField(max_length=128, verbose_name=u'Answer\'s text')
    question = models.ForeignKey(Question, null=True)
    correct = models.BooleanField('Correct', default=True)

    def __str__(self):
        return self.detail

   
