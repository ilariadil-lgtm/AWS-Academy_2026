from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('create', views.create_task, name="create_task"),
    # le rotte specifiche sempre prima delle rotte dinamiche
    path('add-tag', views.add_tag, name="add_tag"),
    path('<str:project_id>', views.get_task, name="get_task"),
]