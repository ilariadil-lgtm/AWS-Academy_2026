from django.db import IntegrityError, OperationalError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
import json
from tag.models import Tag

@csrf_exempt
@require_GET
def get_tags(request):
    try:
        tags = list(Tag.objects.all().values())

        return JsonResponse(tags, safe=False, status=200)
    
    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)

@csrf_exempt
@require_GET
def get_tags_by_task_id(request, task_id):
    try:
        tags = list(Tag.objects.filter(tasks=task_id).values())

        return JsonResponse(tags, safe=False, status=200)
    
    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)



@csrf_exempt
@require_POST
def create_tag(request):
    print('here')
    try: 
        data = json.loads(request.body)

        tag = Tag.objects.create(
            name=data['name']
        )

        return JsonResponse({
            'id': tag.id,
            'name': tag.name
        }, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    
    except KeyError as e:
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)
    
    except IntegrityError:
        return JsonResponse({'error': 'Tag già esistente'}, status=409)


    