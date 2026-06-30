#!/bin/bash
echo "📊 Running Django migrations..."
docker-compose exec backend python manage.py migrate
echo "✅ Migrations complete."
