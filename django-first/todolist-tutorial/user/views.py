from django.shortcuts import render
from .data import user_list

# Create your views here.

from django.http import HttpResponse, JsonResponse

def users(request):
    return JsonResponse(user_list, safe=False)


def user(request, id):
    user = next((u for u in user_list if u.get("id") == id), None)

    if user is None:
        return JsonResponse({"error": "User not found"}, status=404) 


    return JsonResponse(user, safe=False)

