from django.shortcuts import render
from data import user_lists

# Create your views here.

from django.http import HttpResponse, JsonResponse

def users(request):
    return JsonResponse(user_lists)

