from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="post"),
    path("comments/", views.comments, name="comments"),
    path("albums/", views.albums, name="albums"),
    path("photos/", views.photos, name="photos"),
    path("todos/", views.todos, name="todos"),
    path("users/", views.users, name="users"),
]