# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from django.apps import apps

from rest_framework import viewsets
from rest_framework import permissions, authtoken
from rest_framework.decorators import api_view
from rest_framework.response import Response

#from apps.bets.models import Answers
from .serializers import BetsSerializer


class BetsViewSet(viewsets.ModelViewSet):
    Answers = apps.get_model('game', 'Answers')
    queryset = Answers.objects.all()
    serializer_class = BetsSerializer
    permission_classes = (permissions.IsAuthenticated,)


@api_view(['POST'])
def register_bet(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id', 0)
        answer_id = request.POST.get('answer_id', 0)
        Answers = apps.get_model('game', 'Answers')
        Bets = apps.get_model('game', 'Bets')
        print request.POST
        user = User.objects.get(pk=user_id)
        answers = Answers.objects.get(pk=answer_id)
        bet = Bets(
            answers=answers,
            user=user
        )
        bet.save()
        return Response({
            'status': 'ok'
        })
    return Response({
        "status": "error",
        "response": ""
    })


"""
method = "POST"
handler = urllib2.HTTPHandler()
opener = urllib2.build_opener(handler)
data = urllib.urlencode({'user_id':'', answer_id
request = urllib2.Request(url, data=data)
request.add_header("Content-Type",'application/json')
request.get_method = lambda: method
try:
    connection = opener.open(request)
except urllib2.HTTPError,e:
    connection = e

if connection.code == 200:
    data = connection.read()
else:
    pass
"""
