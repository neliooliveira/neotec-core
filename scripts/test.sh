#!/bin/bash
echo "🧪 Running tests..."
docker-compose exec backend python manage.py test
echo "✅ Tests complete."
