import uuid
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
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, verbose_name='Имя заявки')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, verbose_name='Категория')
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

    image = models.ImageField(upload_to='img/',
                              validators=[validate_image_file_extension,
                                          FileExtensionValidator(['bmp', 'jpeg', 'jpg', 'png'],
                              message='Allowed types: bmp, jpeg, jpg. png')],
                              verbose_name='План помещения')

    comment = models.TextField(max_length=1000, verbose_name='Комментарий', blank=True)

    complete_image = models.ImageField(blank=True, upload_to='img/',
                              validators=[validate_image_file_extension,
                                          FileExtensionValidator(['bmp', 'jpeg', 'jpg', 'png'],
                                                                 message='Allowed types: bmp, jpeg, jpg. png')],
                              verbose_name='Готовый дизайн')

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.id)])
