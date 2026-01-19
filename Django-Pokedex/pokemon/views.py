import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Pokemon

def pokemon_list(request):
    if request.method == 'GET':
        pokemons = list(Pokemon.objects.values())
        return JsonResponse(pokemons, safe=False)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def pokemon_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            required_fields = ['nome', 'tipo']
            if not all(field in data for field in required_fields):
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            pokemon = Pokemon.objects.create(
                nome=data['nome'],
                tipo=data['tipo'],
                salute=data.get('salute', 50),
                attacco=data.get('attacco', 50),
                difesa=data.get('difesa', 50),
                attacco_speciale=data.get('attacco_speciale', 50),
                difesa_speciale=data.get('difesa_speciale', 50),
                velocita=data.get('velocita', 50)
            )
            return JsonResponse({
                'id': pokemon.id,
                'nome': pokemon.nome,
                'tipo': pokemon.tipo,
                'salute': pokemon.salute,
                'attacco': pokemon.attacco,
                'difesa': pokemon.difesa,
                'attacco_speciale': pokemon.attacco_speciale,
                'difesa_speciale': pokemon.difesa_speciale,
                'velocita': pokemon.velocita
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def pokemon_delete(request, pk):
    if request.method == 'DELETE':
        try:
            pokemon = Pokemon.objects.get(pk=pk)
            pokemon.delete()
            # Return updated list
            pokemons = list(Pokemon.objects.values())
            return JsonResponse(pokemons, safe=False)
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
