from django.urls import path

from user.views import UserLoginView, CreateUserView, UserProfileView, UserLogoutView,UserProfileUpdateView

urlpatterns = [
    path('register/',CreateUserView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/',UserProfileView.as_view(), name='profile'),
    path('logout/',UserLogoutView.as_view(), name='logout'),
    path('edit/profile/',UserProfileUpdateView.as_view(),name='edit_profile'),

]
