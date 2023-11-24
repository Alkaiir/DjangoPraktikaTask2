from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('applications/', ApplicationListView.as_view(), name='applications'),
    path('application/<uuid:pk>', ApplicationDetailView.as_view(), name='application-detail'),
    path('application/<uuid:pk>/delete', ApplicationDelete.as_view(), name='application-delete'),
    path('application/create/', ApplicationCreate.as_view(), name='application-create'),
    path('application/<uuid:pk>/change/in-work', ApplicationChangeToInWork.as_view(), name='application-update-in-work'),
    path('application/<uuid:pk>/change/complete', ApplicationChangeToComplete.as_view(), name='application-update-complete'),
    path('category-list', CategoryListView.as_view(), name='category-list'),
    path('category/create', CategoryCreate.as_view(), name='category-create'),
    path('category/delete/<int:pk>', CategoryDelete.as_view(), name='category-delete'),

]
