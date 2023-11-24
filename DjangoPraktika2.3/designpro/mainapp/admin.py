from django.contrib import admin


from .models import Category, Application, CustomUser

# Register your models here.

admin.site.register(Category)
admin.site.register(CustomUser)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'category', 'customer', 'status')
    fields = ['title', 'category', 'customer', 'status']