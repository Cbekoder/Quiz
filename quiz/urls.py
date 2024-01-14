from django.urls import path
from .views import QuizListView, QuestionListView, UserQuizView, SubmitUserChoiceView

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('questions/<int:quiz_id>/', QuestionListView.as_view(), name='question_list'),
    path('user_quiz/', UserQuizView.as_view(), name='user_quiz'),
    path('submit_choice/', SubmitUserChoiceView.as_view(), name='submit_user_choice'),
]
