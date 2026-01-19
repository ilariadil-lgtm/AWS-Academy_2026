import requests
import json
import sys

BASE_URL = 'http://127.0.0.1:8000/pokemon'

def test_api():
    print("Testing API...")
    
    # 1. Create a Pokemon
    print("\n[POST] Creating Pikachu...")
    payload = {
        "nome": "Pikachu",
        "tipo": "Elettro",
        "salute": 35,
        "attacco": 55,
        "difesa": 40,
        "attacco_speciale": 50,
        "difesa_speciale": 50,
        "velocita": 90
    }
    try:
        response = requests.post(f"{BASE_URL}/", json=payload)
        if response.status_code == 201:
            print("SUCCESS: Pikachu created.")
            pikachu_id = response.json()['id']
        else:
            print(f"FAILED: Status {response.status_code}, {response.text}")
            sys.exit(1)
    except Exception as e:
        print(f"FAILED: Could not connect to server. {e}")
        sys.exit(1)

    # 2. List Pokemon
    print("\n[GET] Listing Pokemon...")
    response = requests.get(f"{BASE_URL}/list")
    if response.status_code == 200:
        pokemons = response.json()
        print(f"SUCCESS: Found {len(pokemons)} pokemon(s).")
        print(json.dumps(pokemons, indent=2))
    else:
        print(f"FAILED: Status {response.status_code}")

    # 3. Delete Pokemon
    print(f"\n[DELETE] Deleting Pikachu (ID: {pikachu_id})...")
    response = requests.delete(f"{BASE_URL}/delete/{pikachu_id}/")
    if response.status_code == 200:
        print("SUCCESS: Pokemon deleted.")
        remaining = response.json()
        print(f"Remaining pokemon: {len(remaining)}")
    else:
        print(f"FAILED: Status {response.status_code}, {response.text}")

if __name__ == "__main__":
    test_api()
