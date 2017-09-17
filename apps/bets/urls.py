from django.conf.urls import url
from .views import QuestionView, bets_list

urlpatterns = [
    url(r'^$', bets_list, name='bets_list'),
    url(r'^(?P<id_question>\d+)/$', QuestionView.as_view())
]
