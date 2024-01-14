# quiz/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Quiz, Question, Choice, UserQuiz, UserChoice
from .serializers import (
    QuizSerializer, QuestionSerializer, ChoiceSerializer,
    UserQuizSerializer, UserChoiceSerializer
)

class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        return Question.objects.filter(quiz_id=quiz_id)

class UserQuizView(generics.ListCreateAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer

class SubmitUserChoiceView(APIView):
    def post(self, request):
        serializer = UserChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User choice submitted successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Add other quiz-related views as needed
