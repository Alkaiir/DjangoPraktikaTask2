from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from .models import CustomUser


@deconstructible
class FIOValidator(validators.RegexValidator):
    regex = r"^[а-яА-Я]+$"
    message = "Please enter valid details. This value may contain only Cyrillic letters."


@deconstructible
class LoginValidator(validators.RegexValidator):
    regex = r"^[a-zA-Z-]+$"
    message = "Enter a valid login. This value may contain only Latin letters and '-'."


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=150),
    email = forms.EmailField(max_length=50),
    password1 = forms.CharField(max_length=50),
    password2 = forms.CharField(max_length=50),
    first_name = forms.CharField(label='', max_length=150),
    last_name = forms.CharField(label='', max_length=150),
    patronymic = forms.CharField(label='', max_length=150),
    agree_to_processing = forms.BooleanField(label='', required=True, help_text='Согласие на обработку персональных данных')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'patronymic', 'password1', 'password2', 'agree_to_processing']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_username(self):
        username = self.cleaned_data['username']
        validator = LoginValidator()
        try:
            validator(username)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken. Please choose another one.')

        return username

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        validator = FIOValidator()
        try:
            validator(first_name)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        validator = FIOValidator()
        try:
            validator(last_name)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        return last_name

    def clean_patronymic(self):
        patronymic = self.cleaned_data['patronymic']
        validator = FIOValidator()
        try:
            validator(patronymic)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        return patronymic