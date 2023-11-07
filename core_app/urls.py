from django.urls import path, include
from core_app.views import *

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('question/', AskQuestionView.as_view(),name='ask_question'),
    path('question/<slug:question_slug>/', SingleQuestion.as_view(),name='single_question'),
    path('question/<slug:question_slug>/answers/',SingleQuestionAnserView.as_view(),name='single_question_answers'),
    path('question/<slug:question_slug>/answers/<str:ans_id>/<slug:resp>/<str:count>/',SingleAnserView.as_view(),name='answer_response'),
]
