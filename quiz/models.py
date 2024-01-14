from django.db import models
from user.models import User

# models.py
from django.db import models

class Choice(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Question(models.Model):
    text = models.TextField()
    answers = models.ManyToManyField(Choice)

    def __str__(self):
        return self.text

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class UserChoice(models.Model):
    user_quiz = models.ForeignKey(UserQuiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)