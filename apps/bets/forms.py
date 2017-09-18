# -*- coding: utf-8 -*-
from django import forms
from .models import Question, Answer, Bet


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Question
        fields = ('text', 'due_date')
        exclude = ('create_date', 'create_user', 'update_date', 'update_user')
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Ingrese la pregunta.',
                'class': 'form-control'
            }),
            'due_date': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

    def save(self, commit=True):
        return super(QuestionForm, self).save(commit=commit)


class BetForm(forms.ModelForm):

    question = None
    user = None

    def __init__(self, question, user, *args, **kwargs):
        super(BetForm, self).__init__(*args, **kwargs)
        self.question = question
        self.user = user
        self.fields['answer'].label = self.question.text
        self.fields['answer'].queryset = self.question.answers


    class Meta:
        model = Bet
        fields = ('answer',)
        exclude = ('question', 'date', 'user')
        widgets = {
            'answer': forms.Select(attrs={
                'placeholder': 'Type the question.',
                'class': 'form-control'
            }),
        }

    def clean_answer(self):
        if Bet.objects.filter(question=self.question, user=self.user).exists():
            raise forms.ValidationError('You already answered that!.')
        else:
            return self.cleaned_data['answer']
