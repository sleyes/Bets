# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.template import loader
from django.http import HttpResponse
from .forms import PreguntaForm
from .models import Pregunta


@login_required
def bets_list(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = PreguntaForm(data=request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.create_user = request.user
            pregunta.update_user = request.user
            pregunta.save()
    template = loader.get_template('apuestas_list.html')
    pregunta_list = Pregunta.objects.all()
    context = {
        'username': request.user.username,
        'form': form,
        'pregunta_list': pregunta_list
    }
    return HttpResponse(template.render(context, request))
