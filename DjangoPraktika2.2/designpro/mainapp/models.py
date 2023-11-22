import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension, FileExtensionValidator
from django.db import models
from django.urls import reverse


class Category (models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class CustomUser (AbstractUser):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, verbose_name='Отчество')
    username = models.CharField(max_length=200, verbose_name='Логин', unique=True, blank=False)
    email = models.EmailField(verbose_name="Почта", blank=False)

    def __str__(self):
        return self.username


class Application (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    category = models.ManyToManyField(Category)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="User")

    STATUS = (
        ('n', 'New'),
        ('i', 'In Work'),
        ('c', 'Complete'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=False,
        default='n')

    image = models.ImageField(upload_to='media/', default='media/default.png',
                              validators=[validate_image_file_extension,
                                          FileExtensionValidator(['bmp', 'jpeg', 'jpg', 'png'],
                                                                 message='Allowed types: bmp, jpeg, jpg. png')])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.id)])

