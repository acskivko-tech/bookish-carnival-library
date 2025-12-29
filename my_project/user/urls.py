from django.urls import path

from user.views import UserLoginView, CreateUserView, UserProfileView, UserLogoutView

urlpatterns = [
    path('register/',CreateUserView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/',UserProfileView.as_view(), name='profile'),
    path('logout/',UserLogoutView.as_view(), name='logout'),

]
