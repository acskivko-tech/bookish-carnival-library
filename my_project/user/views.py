from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from user.forms import UpdateUserForm


# Create your views here.


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user/register_form.html'
    success_url = reverse_lazy('login')



class UserLoginView(LoginView):
    template_name = 'user/login_form.html'
    authentication_form = AuthenticationForm
    success_url = reverse_lazy('profile')


class UserProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'user/profile.html'


class UserLogoutView(LoginRequiredMixin,TemplateView):
    template_name = 'user/logout.html'

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

class UserProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'user/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
