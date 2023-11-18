from django.urls import path, include
from . import views
from .views import RegisterUser

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', RegisterUser.as_view(), name='register'),
]
