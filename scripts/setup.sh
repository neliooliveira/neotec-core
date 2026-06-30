#!/bin/bash
set -e

echo "🚀 NEOTEC Core Development Setup"
echo "================================"

# Copy env files
echo "📝 Setting up environment files..."
cp .env.example .env
echo "   ✅ .env created from .env.example"

echo ""
echo "🐳 Starting Docker services..."
docker-compose up -d

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

echo ""
echo "🗄️  Running Django migrations..."
docker-compose exec -T backend python manage.py migrate

echo ""
echo "📊 Creating Django superuser..."
docker-compose exec -T backend python manage.py createsuperuser --noinput --username admin --email admin@neotec.com || true

echo ""
echo "✅ Setup complete!"
echo ""
echo "🌐 Access points:"
echo "   - Frontend:        http://localhost:3000"
echo "   - Backend API:     http://localhost:8000/api"
echo "   - Admin:           http://localhost:8000/admin"
echo ""
echo "📖 Documentation:"
echo "   - Project Charter: docs/00-project-charter.md"
echo "   - Architecture:    docs/03-architecture.md"
echo ""
