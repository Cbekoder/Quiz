from rest_framework import serializers
from .models import Quiz, Question, Choice, UserQuiz, UserChoice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'

class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = '__all__'
class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'
class UserQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuiz
        fields = ('id', 'user', 'quiz', 'score')

class UserChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChoice
        fields = ('id', 'user_quiz', 'question', 'choice')