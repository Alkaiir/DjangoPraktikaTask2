from django.contrib import admin


from .models import Category, Application, CustomUser

# Register your models here.

admin.site.register(Category)
admin.site.register(Application)
admin.site.register(CustomUser)



