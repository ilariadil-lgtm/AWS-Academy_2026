from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.get_pokemon_list, name="get_pokemon_list"),
    path('add_pokemon/', views.add_pokemon, name='add_pokemon'),
    #path('',admin.site.urls),
   # path("delete/<str:id>", views.delete_pokemon, name="delete_pokemon"), 
   # path("update/patch/<str:id>", views.update_patch_pokemon, name="update_patch_pokemon"), 
   # path("update/put/<str:id>", views.update_put_pokemon, name="update_put_pokemon"), 
]
