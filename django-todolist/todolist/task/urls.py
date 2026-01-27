from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('create', views.create_task, name="create_task"),
    path('<str:project_id>', views.get_task, name="get_task"),
]
