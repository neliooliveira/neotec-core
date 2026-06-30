#!/bin/bash
echo "📝 Making new Django migrations..."
docker-compose exec backend python manage.py makemigrations
echo "✅ Migrations created."
