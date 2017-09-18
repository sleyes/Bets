# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Answer, Bet


def add_simbol_text(modeladmin, request, queryset):
    for q in queryset:
        q.text = q.text + '?'
        q.save()
add_simbol_text.short_description = 'Add question mark (?)'


class AnswerHeadInLine(admin.TabularInline):
    model = Answer
    extra = 1
    readonly_fields = ('create_user', 'update_user')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'create_user')
    search_fields = ('text', 'create_user__username')
    list_filter = ('text',)
    inlines = [AnswerHeadInLine, ]
    actions = [add_simbol_text, ]

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'text')

admin.site.register(Answer, AnswerAdmin)

admin.site.register(Bet)
