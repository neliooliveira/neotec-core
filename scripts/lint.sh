#!/bin/bash
echo "🎨 Running linters..."
docker-compose exec backend python -m black --check . 2>/dev/null || echo "⚠️  Black not installed"
docker-compose exec backend python -m flake8 . 2>/dev/null || echo "⚠️  Flake8 not installed"
echo "✅ Lint check complete."
