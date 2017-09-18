# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import View

from .forms import QuestionForm
from .models import Question


@login_required
def bets_list(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_user = request.user
            question.update_user = request.user
            question.save()
    template = loader.get_template('bets_list.html')
    question_list = Question.objects.all()
    context = {
        'username': request.user.username,
        'form': form,
        'question_list': question_list
    }
    return HttpResponse(template.render(context, request))


class QuestionView(LoginRequiredMixin, View):
    form = QuestionForm()
    template_name = "question_form.html"

    def get(self, request, *args, **kwargs):
        id_question = self.kwargs['id_question']
        prg = Question.objects.get(pk=id_question)
        form = QuestionForm(instance=prg)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id_question = self.kwargs['id_question']
        prg = Question.objects.get(pk=id_question)
        form = QuestionForm(data=request.POST, instance=prg)
        if form.is_valid():
            prg = form.save(commit=False)
            prg.save()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


@login_required
def bet(request, id_question):
    template = loader.get_template('bet.html')
    question = Question.objects.get(pk=id_question)
    form = QuestionForm(question, request.user)
    if request.method == 'POST':
        form = BetForm(question, request.user, data=request.POST)
        if form.is_valid():
            respuesta_apuesta = form.save(commit=False)
            respuesta_apuesta.user = request.user
            respuesta_apuesta.save()
    context = {
        'question': question,
        'form': form
    }
    return HttpResponse(template.render(context, request))
