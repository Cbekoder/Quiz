from django.contrib import admin
from .models import Choice, Question, Quiz, UserQuiz, UserChoice

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(UserChoice)
admin.site.register(UserQuiz)
