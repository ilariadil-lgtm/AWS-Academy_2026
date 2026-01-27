#!/bin/bash

echo "======================="
echo "start activaction venv"
echo "======================="

source venv/bin/activate

echo "======================="
echo "venv in esecuzione"
echo "======================="

echo "======================="
echo "ti trovi in:"
pwd
echo "======================="

python manage.py runserver