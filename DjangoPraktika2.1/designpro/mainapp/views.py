from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .models import Category, Application
from .forms import RegisterUserForm


def index(request):

    in_work = Application.objects.filter(status__exact='i').count()

    return render(request, 'index.html', context={'design': in_work})


class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'mainapp/register.html'
    success_url = reverse_lazy('login')
