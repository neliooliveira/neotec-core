#!/bin/bash
set -e

echo "🚀 NEOTEC Core Development Setup"
echo "================================="

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

echo ""
echo "📁 Project directory: $PROJECT_ROOT"

# Check if .env.example exists, if not create it
if [ ! -f ".env.example" ]; then
    echo "⚠️  .env.example not found, creating from template..."
    cat > .env.example << 'ENVEOF'
# Django Settings
DJANGO_SECRET_KEY=django-insecure-dev-change-in-production
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,backend
DJANGO_ENVIRONMENT=development

# Database
DATABASE_NAME=neotec_core
DATABASE_USER=neotec
DATABASE_PASSWORD=neotec_password_dev
DATABASE_HOST=postgres
DATABASE_PORT=5432

# Valkey (Redis)
VALKEY_URL=redis://valkey:6379/0
CACHE_URL=redis://valkey:6379/1

# Email
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000/api
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Celery
CELERY_BROKER_URL=redis://valkey:6379/2
CELERY_RESULT_BACKEND=redis://valkey:6379/3

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000

# Caddy
CADDY_EMAIL=admin@neotec.com
ENVEOF
    echo "   ✅ .env.example created"
fi

# Copy .env from .env.example if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env from .env.example..."
    cp .env.example .env
    echo "   ✅ .env created"
else
    echo "   ℹ️  .env already exists"
fi

echo ""
echo "🐳 Starting Docker services..."
docker-compose up -d

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

echo ""
echo "🔄 Checking service status..."
docker-compose ps

echo ""
echo "✅ Setup complete!"
echo ""
echo "🌐 Access points:"
echo "   - Frontend:        http://localhost:3000"
echo "   - Backend API:     http://localhost:8000/api"
echo "   - Admin:           http://localhost:8000/admin"
echo "   - Caddy:           http://localhost"
echo ""
echo "📖 Documentation:"
echo "   - Project Charter: docs/00-project-charter.md"
echo "   - Architecture:    docs/03-architecture.md"
echo "   - Development:     DEVELOPMENT.md"
echo ""
echo "🆘 If something fails, try:"
echo "   docker-compose logs backend"
echo "   docker-compose logs frontend"
echo ""
