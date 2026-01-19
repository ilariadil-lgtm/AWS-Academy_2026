from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pippo/", views.pippo, name="pippo"),
    path("user/", views.user, name="user"),
] 