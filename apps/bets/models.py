# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.CharField(max_length=200)
    due_date = models.DateTimeField('Due Date')
    create_date = models.DateTimeField('Creation date', auto_now_add=True)
    create_user = models.ForeignKey(User, related_name="question_create_user")
    update_date = models.DateTimeField('Update date', auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="question_update_user")

    def __unicode__(self):
        return "%s" % self.text

    @property
    def answers(self):
        return Answer.objects.filter(question=self)

    def get_result(self):
        answers = Answer.objects.filter(question=self)
        dic = []
        for x in answers:
            dic.append((x.text, Bet.objects.filter(answer=x).count()))
        return dic


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=20)
    create_date = models.DateTimeField('Creation date', auto_now_add=True)
    create_user = models.ForeignKey(User, related_name="answer_create_user")
    update_date = models.DateTimeField('Update date', auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="answer_update_user")

    class Meta:
        unique_together = ('question', 'text')

    def __unicode__(self):
        return "%s" % self.text

    @property
    def question_text(self):
        return self.question.text


class Bet(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question, blank=True, null=True)
    answer = models.ForeignKey(Answer)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'question')

    def __unicode__(self):
        return "%s - %s" % (self.user.username, self.question.text)

    def save(self, *args, **kwargs):
        self.question = self.answer.question
        return super(Bet, self.save(*args, **wkargs))
