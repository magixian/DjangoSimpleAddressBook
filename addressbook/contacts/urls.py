from django.contrib import admin
from django.urls import path
from .import views

app_name = 'contacts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('view/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>/', views.add, name='edit'),
    path('save/', views.save, name='save'),
    path('update/<int:pk>/', views.save, name='update'), # update url will use the function with save
    path('delete/<int:pk>/', views.delete, name='delete'),
]
