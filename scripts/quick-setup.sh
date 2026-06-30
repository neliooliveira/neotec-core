#!/bin/bash
# Quick manual setup for NEOTEC Core

echo "🚀 NEOTEC Core - Quick Manual Setup"
echo "====================================="
echo ""
echo "✅ Step 1: Create .env file"
cat > .env << 'EOF'
DJANGO_SECRET_KEY=django-insecure-dev-12345
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,backend
DATABASE_NAME=neotec_core
DATABASE_USER=neotec
DATABASE_PASSWORD=neotec_pass
DATABASE_HOST=postgres
DATABASE_PORT=5432
VALKEY_URL=redis://valkey:6379/0
CACHE_URL=redis://valkey:6379/1
CELERY_BROKER_URL=redis://valkey:6379/2
CELERY_RESULT_BACKEND=redis://valkey:6379/3
NEXT_PUBLIC_API_URL=http://localhost:8000/api
CORS_ALLOWED_ORIGINS=http://localhost:3000
EOF
echo "   ✅ .env created"

echo ""
echo "✅ Step 2: Start Docker containers"
docker-compose up -d
echo "   ✅ Waiting 10 seconds for services..."
sleep 10

echo ""
echo "✅ Step 3: Run migrations"
docker-compose exec -T backend python manage.py migrate 2>/dev/null || true

echo ""
echo "🌟 Services running!"
echo ""
echo "Frontend:  http://localhost:3000"
echo "Backend:   http://localhost:8000/api"
echo "Admin:     http://localhost:8000/admin"
echo ""
echo "View logs: docker-compose logs -f"
