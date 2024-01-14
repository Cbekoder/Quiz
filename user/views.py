from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from quiz.models import UserQuiz
from quiz.serializers import UserQuizSerializer
from .serializers import UserSerializer
from rest_framework import status

class UserCreateView(generics.CreateAPIView):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileView(APIView):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

class UserQuizzesView(APIView):
    def get(self, request):
        user = request.user
        user_quizzes = UserQuiz.objects.filter(user=user)
        user_quizzes_serializer = UserQuizSerializer(user_quizzes, many=True)

        return Response(user_quizzes_serializer.data, status=status.HTTP_200_OK)

