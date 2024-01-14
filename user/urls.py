from django.urls import path
from .views import UserCreateView, UserProfileView, UserQuizzesView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/my_quizzes/', UserQuizzesView.as_view(), name='user_quizzes'),
]
