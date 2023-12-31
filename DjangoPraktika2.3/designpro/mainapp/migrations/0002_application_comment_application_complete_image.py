# Generated by Django 4.2.7 on 2023-11-23 13:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='application',
            name='complete_image',
            field=models.ImageField(blank=True, upload_to='img/', validators=[django.core.validators.validate_image_file_extension, django.core.validators.FileExtensionValidator(['bmp', 'jpeg', 'jpg', 'png'], message='Allowed types: bmp, jpeg, jpg. png')], verbose_name='Готовый дизайн'),
        ),
    ]
