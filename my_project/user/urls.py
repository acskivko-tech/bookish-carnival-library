from django.urls import path

from user.views import UserLoginView, CreateUserView, UserProfileView

urlpatterns = [
    path('register/',CreateUserView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/',UserProfileView.as_view(), name='profile'),

]
