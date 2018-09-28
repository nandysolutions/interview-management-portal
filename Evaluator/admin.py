# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Candidate
from .models import Position
from .models import Interview
from .models import Question, Answer
from .models import Skill
from .models import QuestionSet
from .models import Round
from .models import Vendor
from .models import RatingSheet, Aspect

class VendorAdmin(admin.ModelAdmin):
    model = Position
    list_display = ('name', 'v_type')

class PositionAdmin(admin.ModelAdmin):
    model = Position
    list_display = ('__str__', 'id_code','exp_needed', 'location', 'j_type')

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['description']
    list_filter = ['difficulty', 'skill']
    list_display = ('description', 'difficulty', 'skill')
    fieldsets = [
        (None,               {'fields': ['description', 'difficulty', 'skill', 'qset']}),

    ]
    inlines = [AnswerInline]

class RoundInline(admin.TabularInline):
    model = Round
    extra = 0

class InterviewAdmin(SimpleHistoryAdmin):
    list_display = ('__str__', 'candidate','date', 'position', 'status', 'result')
    search_fields = ['candidate__name']
    list_editable = ['status', 'result']
    list_filter = ['status', 'result']
    history_list_display = ["status", "result"]

    inlines = [RoundInline]

class AspectInline(admin.TabularInline):
    model = Aspect
    extra = 0


class RatingSheetAdmin(admin.ModelAdmin):
    def aspects_count(self, obj):
        return obj.aspect_set.count()

    list_display = ('name', 'rate_min', 'rate_max', 'aspects_count')
    model = RatingSheet
    inlines = [AspectInline]


admin.site.register(Vendor, VendorAdmin)
admin.site.register(Candidate)
admin.site.register(Position, PositionAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Skill)
admin.site.register(QuestionSet)
admin.site.register(RatingSheet, RatingSheetAdmin)
