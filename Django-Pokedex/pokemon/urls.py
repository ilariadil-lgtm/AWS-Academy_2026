from django.urls import path
from . import views

urlpatterns = [
    path('list', views.pokemon_list, name='pokemon_list'),
    path('', views.pokemon_create, name='pokemon_create'),
    path('delete/<int:pk>/', views.pokemon_delete, name='pokemon_delete'),
]
