from django.urls import path
from .views import (
    QuizListView, 
    QuizView,
    QuizDataView,
    saveQuizView
)

app_name = 'quizes'
urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', QuizView.as_view(), name='quiz-view'),
    path('<pk>/save/', saveQuizView.as_view(), name='save-view'),
    path('<pk>/data/', QuizDataView.as_view(), name='quiz-data-view'),
]