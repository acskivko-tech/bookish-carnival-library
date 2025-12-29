from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, TemplateView


# Create your views here.


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user/register_form.html'


class UserLoginView(LoginView):
    template_name = 'user/login_form.html'
    authentication_form = AuthenticationForm


class UserProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'user/profile.html'
