from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_tags, name="get_tags"),
    path('create', views.create_tag, name="create_tag"),
    path('task/<str:task_id>', views.get_tags_by_task_id, name="get_tags_by_task_id"),
]
