# -*- coding: utf-8 -*-
from django.apps import apps

from rest_framework import serializers


class BetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        Answer = apps.get_model('bets', 'Answer')
        model = Answer
        fields = ('id', 'question_text', 'question_id', 'text')
