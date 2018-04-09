from django.contrib import admin
from django.urls import path
from .import views

app_name = 'contacts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('view/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.add, name='add'),
    path('save/', views.save, name='save'),
]
