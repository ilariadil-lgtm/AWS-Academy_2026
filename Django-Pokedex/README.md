# Pokedex API (Django)

Backend application developed in Django to manage a list of Pokémon stored in a SQLite database.

## Environment

- macOS
- Python 3
- Django

## Project Setup

### 1. Clone the repository

```bash
git clone <repository_url>
cd pokedex_project
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

## Database & Migrations

Run migrations to create the database and the Pokemon table:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Start the Server

### 1. Activate virtual environment (if not already active)

```bash
source venv/bin/activate
```

### 2. Run the server

```bash
python manage.py runserver
```

**Alternative (one-line command):**
```bash
./venv/bin/python manage.py runserver
```

Open in browser:
- http://127.0.0.1:8000/pokemon/list

## API Endpoints

### LIST - Get all Pokémon
**GET** `/pokemon/list`

Example:
```bash
curl http://127.0.0.1:8000/pokemon/list
```

### CREATE - Add a new Pokémon
**POST** `/pokemon/`

Body (JSON):
- `nome` (required)
- `tipo` (required)
- `salute` (default 50)
- `attacco` (default 50)
- `difesa` (default 50)
- `attacco_speciale` (default 50)
- `difesa_speciale` (default 50)
- `velocita` (default 50)

Example:
```bash
curl -X POST http://127.0.0.1:8000/pokemon/ \
     -H "Content-Type: application/json" \
     -d '{"nome":"Bulbasaur","tipo":"Erba/Veleno","salute":45,"attacco":49}'
```

### DELETE - Remove a Pokémon
**DELETE** `/pokemon/delete/<id>/`

Example (delete Pokemon with ID 1):
```bash
curl -X DELETE http://127.0.0.1:8000/pokemon/delete/1/
```
