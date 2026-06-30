#!/bin/bash
echo "🗑️  Reverting Django migrations..."
docker-compose exec backend python manage.py migrate $1 0
echo "✅ Migrations reverted."
