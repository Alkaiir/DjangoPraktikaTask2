from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('applications/', ApplicationListView.as_view(), name='applications'),
    path('application/<uuid:pk>', ApplicationDetailView.as_view(), name='application-detail'),
    path('application/<uuid:pk>/delete', ApplicationDelete.as_view(), name='application-delete'),
    path('application/create/', views.ApplicationCreate.as_view(), name='application-create'),
]
