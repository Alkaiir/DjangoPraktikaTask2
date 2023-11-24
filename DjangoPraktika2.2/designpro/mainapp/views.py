from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View, generic
from django.views.generic import CreateView, DeleteView

from .models import Category, Application
from .forms import *


def index(request):

    in_work = Application.objects.filter(status__exact='i').count()
    complete = Application.objects.filter(status__exact='c').order_by('-time')[:4]

    return render(request, 'index.html', context={'in_work': in_work, 'complete': complete})


class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'mainapp/register.html'
    success_url = reverse_lazy('login')


def profile(request):

    applications = Application.objects.filter(customer=request.user).order_by('-time')
    new_applications = Application.objects.filter(customer=request.user).filter(status__exact='n').order_by('-time')
    in_work_applications = Application.objects.filter(customer=request.user).filter(status__exact='i').order_by('-time')
    complete_applications = Application.objects.filter(customer=request.user).filter(status__exact='c').order_by('-time')

    form = ApplicationsSort()

    if request.method == 'POST':
        form = ApplicationsSort(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['dropdown']
    return render(request, 'mainapp/profile.html', context={'applications': applications,
                                                            'form': form,
                                                            'new_applications': new_applications,
                                                            'in_work_applications': in_work_applications,
                                                            'complete_applications': complete_applications})


class ApplicationListView(generic.ListView):

    model = Application
    paginate_by = 10


class ApplicationDetailView(generic.DetailView):
    model = Application


class ApplicationCreate(CreateView):
    model = Application
    fields = ['title', 'description', 'category', 'image']
    template_name = 'mainapp/application_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.customer = self.request.user
        instance.save()

        return redirect('profile')

    def clean_image(self):
        image = self.cleaned_data.get("image")
        image_size = image.size
        str_file = str(image)
        if str_file.endswith('.jpg') and image_size <= 2097152:
            return image
        elif str_file.endswith('.jpeg') and image_size <= 2097152:
            return image
        elif str_file.endswith('.png') and image_size <= 2097152:
            return image
        elif str_file.endswith('.bpm') and image_size <= 2097152:
            return image
        else:
            raise ValidationError(
                "Ошибка: "
                "Файл не является форматом: jpg, jpeg, png, bmp или его размер больше 2Мб."
            )


class ApplicationDelete(DeleteView):
    model = Application
    success_url = '../../profile'
    template_name = 'mainapp/application_form_delete.html'

