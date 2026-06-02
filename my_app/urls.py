from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forms/', views.forms, name='forms'),
    path('edit/<str:id>/', views.edit, name='edit'),
    path('delete/<str:id>/', views.delete, name='delete')
]