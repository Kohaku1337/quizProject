from django.urls import path
from berebere.quiz.views import *

urlpatterns = [
    path('', GetQuestion.as_view()),
    path('answer/', QuestionAnswer.as_view()),
]